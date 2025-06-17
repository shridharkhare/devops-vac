from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/health")
def health_check():
    return "OK", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
