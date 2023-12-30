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
    date_created = db.Column(db.DateTime, nullable=True, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"User('{self.title}','{self.text}')"

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'date': self.date_created
        }


with app.app_context():
    db.create_all()
    notifications = Notifications()
    notifications.title = 'refactor app'
    notifications.text = 'test 1234'
    db.session.add(notifications)
    db.session.commit()

users = [{"name": "marko", "age": "33", "id": "123153765"}, {"name": "marko", "age": "33", "id": "123153765"}]


@app.route("/", methods=['GET'])
def generate_user():
    return users


@app.route("/notifications/all", methods=['GET'])
def set_notifications():
    all_notifications = Notifications.query.all()
    result = [notification.serialize() for notification in all_notifications]
    return jsonify(result), 200


@app.route("/notifications/create", methods=['POST'])
# TODO remove, change in postman
def get_notifications():
    notification1 = Notifications()
    notification1.title = 'test1title'
    notification1.text = 'text2test'
    db.session.add(notification1)
    db.session.commit()
    all_users = db.session.execute(db.select(Notifications)).scalar()
    return jsonify([all_users.title, all_users.text])


@app.route("/api/notifications", methods=['GET', 'POST'])
def users_change():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        notification1 = Notifications()
        notification1.title = title
        notification1.text = text
        db.session.add(notification1)
        db.session.commit()

    all_notifications = Notifications.query.all()
    result = [notification.serialize() for notification in all_notifications]
    return make_response(jsonify(result), 200)



if __name__ == "__main__":
    app.run(port=5000)
