import math



def convert_to_pic50(input_data):
    allowed_units = ["milli", "micro", "nano"]
    status = {}
    
    status["status"] = False
    status["message"] = ""
    status["pic_50"] = None

    ic_50 = None
    unit = ""
    
    if "ic_50" in input_data:
        ic_50 = input_data["ic_50"]
    
        if type(ic_50) is float:
            status["message"] = "IC 50 not float"
            return status
    else:
        status["message"] = "IC 50 not found"
        return status

    if "unit" in input_data:
        unit = input_data["unit"]

        if unit not in allowed_units:
            status["message"] = "Unit not allowed"
            return status
    else:
        status["message"] = "Unit not found"
        return status

    molar_val = convert_to_molar(ic_50, unit)
    
    if molar_val is not None:
        status["pic_50"] = math.log10(1/molar_val)
        status["status"] = True
        status["message"] = "Calculated pic50"
    else:
        status["message"] = "Issue calculating pic50"
        return status

    return status

def convert_to_molar(value, unit):
    molar_value = None
    
    try:
        if unit == "nano":
            molar_value = value * pow(10, -9)
        elif unit == "micro":
            molar_value = value * pow(10, -6)
        elif unit == "milli":
            molar_value = value * pow(10, -3)
    except:
        pass

    return molar_value
