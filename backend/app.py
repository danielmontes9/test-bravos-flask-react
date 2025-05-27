from flask import Flask, jsonify, request

app = Flask(__name__)

# Hello World endpoint
@app.route('/hello', methods=['GET'])
def get_items():
    return "hello world!"


if __name__ == '__main__':
    app.run(debug=True)