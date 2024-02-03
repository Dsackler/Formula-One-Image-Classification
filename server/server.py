from flask import Flask, request, jsonify
from flask_cors import CORS
import util
import base64

app = Flask(__name__)
CORS(app)

@app.route('/classify_image', methods = ['GET', 'POST'])
def classify_image():
    # image_data = request.form['image_data']
    # response = jsonify(util.classify_image(image_data))
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return response
    image_data = request.files['file'].read()
    print(image_data)
    # bytes_data = image_data.encode('utf-8')
    # bytes_data = image_data.decode('utf-8')
    # print(type(image_data))
    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print('Starting Flask Server')
    util.load_saved_artifiacts()
    app.run(port = 5000)