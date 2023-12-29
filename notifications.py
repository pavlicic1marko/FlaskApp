import datetime
from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
# database location ///- this folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notifications.sqlite'
# create database instance
db = SQLAlchemy()
db.init_app(app)


class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"User('{self.title}','{self.text}')"

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
        }


with app.app_context():
    db.create_all()

users = [{"name": "marko", "age": "33", "id": "123153765"}, {"name": "marko", "age": "33", "id": "123153765"}]
news = [{"title": "GDP jumps 10 times", "text": "GDP of astocka hase increased 10 times"}]


@app.route("/", methods=['GET'])
def generate_user():
    return users


@app.route("/notifications/all", methods=['GET'])
def set_notifications():
    all_notifications = Notifications.query.all()
    result = [notification.serialize() for notification in all_notifications]
    return jsonify(result)


@app.route("/notifications/create", methods=['POST'])
def get_notifications():
    notifications=Notifications()
    notifications.title = 'test1title'
    notifications.text = 'text2test'
    db.session.add(notifications)
    db.session.commit()
    all_users = db.session.execute(db.select(Notifications)).scalar()
    return jsonify([all_users.title,all_users.text])



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
