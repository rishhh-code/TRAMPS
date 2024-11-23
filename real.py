from flask import Flask,request,jsonify
import requests

app = Flask(__name__)

@app.route('/hello',methods = ['POST'])
def hello():
    url = 'http://tnagriculture.in/mannvalam/soils/en'
    data = {
        'district' : 610,
        'block' : 6257,
        'village' : 636348,
        'Survey_no' : 2,
        'ownerName' : "\u0baa\u0bbf\u0b9a\u0bcd\u0b9a\u0bae\u0bc1\u0ba4\u0bcd\u0ba4\u0bc1",
        'mobileNumber' : 8110031124
    }
    response  = requests.post(url,json = data)

    return jsonify(response.json()),response.status_code

if __name__ == '__main__':
    app.run()