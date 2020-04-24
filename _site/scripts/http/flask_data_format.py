from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    format = request.args.get("format", "text")
    if format == "json":
        return jsonify(message="Hello World")
    else:
        return 'Hello World!'


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)

