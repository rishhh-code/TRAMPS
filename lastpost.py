from Beautifulsoup import soil_test_id,lime
from flask import Flask,request,jsonify
import requests




app = Flask(__name__)

@app.route('/',methods = ['POST'])
def hello():
    url = "http://tnagriculture.in/mannvalam/Welcome/soilDatapublic"
    data={
    'soil_test_id' : soil_test_id,
    'lime' : lime
}
    response  = requests.post(url,json = data)

    return jsonify(response.json()),response.status_code

if __name__ == '__main__':
    app.run(debug=True)
