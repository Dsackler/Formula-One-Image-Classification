from flask import Flask, request, jsonify
# import util

app = Flask(__name__)

@app.route('/classify_image', methods = ['GET', 'POST'])
def classify_image():
    return "hello"

if __name__ == "__main__":
    app.run(port = 5000)