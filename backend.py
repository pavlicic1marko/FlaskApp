from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def generate_user():
    return [{"name": "marko", "age": "33", "id": "123153765"},{"name": "marko", "age": "33", "id": "123153765"}]


if __name__ == "__main__":
    app.run(port=5000)