from flask import Blueprint, request, url_for, redirect, make_response, jsonify
import sys, json
from services import converter

main = Blueprint('main', __name__)

@main.route('/api/convert-to-pic50', methods=["POST"])
def convert_to_pic50():
    content = {}
    content["status"] = False
    content["message"] = ""
    content["pic_50"] = None
    
    input_data = None

    try:
        input_data = json.loads(request.get_data())
    except:
        content["message"] = "Issue getting input data"
        return content
    
    if type(input_data) is not dict:
        content["message"] = "Input data is not dict"
        return content
    
    content = converter.convert_to_pic50(input_data)

    return jsonify(content)





