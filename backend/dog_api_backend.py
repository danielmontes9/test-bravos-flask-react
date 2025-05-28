from flask import Flask, jsonify, request
import urllib.request
import json

app = Flask(__name__)

# Hello World endpoint
@app.route('/hello', methods=['GET'])
def get_hello():
    return "hello world!"

@app.route('/breeds', methods=['GET'])
def get_breeds():
    try:
        with urllib.request.urlopen('https://dogapi.dog/api/v2/breeds') as response:
            data = response.read()
            breeds = json.loads(data)

        return json.dumps(breeds), 200, {'Content-Type': 'application/json'}

    except Exception as e:
        return json.dumps({'error': str(e)}), 500, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True, port=5000)