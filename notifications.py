from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

users = [{"name": "marko", "age": "33", "id": "123153765"},{"name": "marko", "age": "33", "id": "123153765"}]
news = [{"title": "GDP jumps 10 times", "text": "GDP of astocka hase increased 10 times"}]



@app.route("/", methods=['GET'])
def generate_user():
    return users

@app.route("/api/notifications", methods=['GET','POST'])
def users_change():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        news.append({"title": title, "text": text})
        return make_response(jsonify(news), 200)

    if request.method == 'GET':
        return make_response(jsonify(news), 200)


if __name__ == "__main__":
    app.run(port=5000)