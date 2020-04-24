import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("Process {} received request on '/'".format(os.getpid()))
    return 'Hello World!'

@app.route('/get_json')
def get_json():
    return jsonify(message="Hello world")

@app.route('/user/<username>')
def show_user_profile(username):
    message = "Hello {}!".format(username)
    return message


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

