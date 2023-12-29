import datetime
from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# database location ///- this folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# create database instance
db = SQLAlchemy(app)


class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.UTC )

    def __repr__(self):
        return f"User('{self.title}','{self.text}')"


users = [{"name": "marko", "age": "33", "id": "123153765"}, {"name": "marko", "age": "33", "id": "123153765"}]
news = [{"title": "GDP jumps 10 times", "text": "GDP of astocka hase increased 10 times"}]


@app.route("/", methods=['GET'])
def generate_user():
    return users


@app.route("/api/notifications", methods=['GET', 'POST'])
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
