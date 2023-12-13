from flask import Flask, jsonify, render_template, request
from markupsafe import escape
import sqlite3

app = Flask(__name__, template_folder='templates')


def database_connection():
    conn = None
    try:
        conn = sqlite3.connect('cars.sqlite')
    except sqlite3.Error as e:
        print(e)
    return conn


@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/test')
def test():
    return jsonify({"users": "testss"})


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/cars', methods=['GET', 'POST'])
def cars():
    conn = database_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM cars")
        car_list = [
            dict(id=row[0], model=row[1], price=row[2])
            for row in cursor.fetchall()
        ]
        if len(car_list) == 0:
            return 'no cars exist', 200
        if car_list is not None:
            return jsonify(car_list)

    if request.method == 'POST':
        new_model = request.form['model']
        new_price = request.form['price']
        sql = """INSERT INTO cars (model, price) VALUES (?, ?)"""

        cursor = cursor.execute(sql, (new_model, new_price))
        conn.commit()
        return f"Car with the id: {cursor.lastrowid} created sucessfully"


@app.route('/cars/<int:car_id>', methods=['GET', 'PUT', 'DELETE'])
def single_car(car_id):
    conn = database_connection()
    cursor = conn.cursor()
    car = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM cars WHERE id=?", (car_id,))
        rows = cursor.fetchall()
        for r in rows:
            car = r
        if car is not None:
            return jsonify(car), 200
        elif len(rows) == 0:
            return "no cars"
        else:
            return "car does not exist or there is an error"
    if request.method == 'PUT':
        sql = """UPDATE cars SET model=?, price=? WHERE id=?"""
        new_model = request.form['model']
        new_price = request.form['price']
        conn.execute(sql, (new_model, new_price, car_id))
        conn.commit()
        return 'request is sent to db'  # TODO return what was changed

    if request.method == 'DELETE':
        sql = """DELETE FROM cars WHERE id=?"""
        conn.execute(sql, (car_id,))
        conn.commit()
        return "the car is deleted"


if __name__ == '__main__':
    app.run(debug=True, port=80)
