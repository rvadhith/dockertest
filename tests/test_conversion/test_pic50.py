from project import create_app


def test_pic50_conversion(client):
    response = client.post("/api/convert-to-pic50", json={
    "ic_50": 1,
    "unit": "nano"
    })
    print(response)
    assert response.json["pic_50"] == 9.0
