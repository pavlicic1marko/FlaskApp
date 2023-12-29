from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

users = [{"name": "marko", "age": "33", "id": "123153765"},{"name": "marko", "age": "33", "id": "123153765"}]
news = [{"title": "marko", "text": "33"}]


@app.route("/", methods=['GET'])
def generate_user():
    return users

@app.route("/users/change", methods=['POST'])
def users_change():
    data = request.form['password']
    return make_response(jsonify(data), 200)

if __name__ == "__main__":
    app.run(port=5000)