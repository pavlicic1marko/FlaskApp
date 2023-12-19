import random
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def test():
    return 'hellow from docker'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
