from flask import jsonify, request, make_response
from notifications import app, db
from notifications.models.user import Notifications

users = [{"name": "marko", "age": "33", "id": "123153765"}, {"name": "marko", "age": "33", "id": "123153765"}]


@app.route("/users", methods=['GET'])
def generate_user():
    response = make_response(jsonify(users), 200)
    response.headers["Access-Control-Allow-Methods"] = "GET"
    return users


@app.route("/notifications/all", methods=['GET'])
def set_notifications():
    all_notifications = Notifications.query.all()
    result = [notification.serialize() for notification in all_notifications]
    return jsonify(result), 200


@app.route("/notifications/<user_id>", methods=['GET', 'DELETE', 'PUT'])
def get_or_delete_notification_by_id(user_id):
    if request.method == 'GET':
        result = Notifications.query.filter_by(id=user_id).first().serialize()
        return jsonify(result), 200

    if request.method == 'DELETE':
        result = Notifications.query.filter_by(id=user_id).delete()
        if result == 0:
            return 'there is no notification with id:' + user_id, 404
        if result == 1:
            db.session.commit()
            return 'deleted notification with id:' + user_id, 201
        return 'Error', 500

    if request.method == 'PUT':
        title = request.form['title']
        text = request.form['text']
        notification = Notifications.query.filter_by(id=user_id).update({"title": title, "text": text})
        db.session.commit()
        return 'updated'


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
    response = make_response(jsonify(result), 200)
    response.headers["Access-Control-Allow-Methods"] = "GET, POST"
    return response
