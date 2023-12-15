import random

from flask import Flask, jsonify, render_template, request
from markupsafe import escape
import sqlite3
import psycopg2

app = Flask(__name__, template_folder='templates')


def database_connection_sqlite():
    conn = None
    try:
        conn = sqlite3.connect('cars.sqlite')
    except sqlite3.Error as e:
        print(e)
    return conn


def database_connection_postgresql():
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", dbname="FlaskCars", user="postgres", password="admin123", port="5432")
    except psycopg2.Error as e:
        print(e)
    return conn


@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/test', methods=['GET', 'POST'])
def test():
    conn = database_connection_postgresql()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM cars")
        return cursor.fetchall()

    if request.method == 'POST':
        new_model = request.form['model']
        new_price = request.form['price']
        cursor.execute("""INSERT INTO cars (id,model, price) VALUES (%s, %s, %s)""",
                       (random.randint(100000000, 900000000), new_model, new_price,))
        conn.commit()
        cursor.execute("SELECT * FROM cars")
        return cursor.fetchall()


@app.route('/test/<int:car_id>', methods=['GET', 'PUT', 'DELETE'])
def test_get_one_car(car_id):
    conn = database_connection_postgresql()
    cursor = conn.cursor()
    if request.method == 'DELETE':
        cursor.execute("""DELETE FROM cars WHERE id= %s""", (car_id,))
        conn.commit()
        cursor.execute("SELECT * FROM cars")
        return cursor.fetchall()

    if request.method == 'GET':
        cursor.execute("""SELECT * FROM cars WHERE id = %s""", (car_id,))
        return cursor.fetchall()
    if request.method == 'PUT':
        new_model = request.form['model']
        new_price = request.form['price']
        cursor.execute("""UPDATE cars SET model=%s, price=%s WHERE id=%s""", ( new_model, new_price, car_id))
        conn.commit()
        cursor.execute("SELECT * FROM cars")
        return cursor.fetchall()
        pass


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/cars', methods=['GET', 'POST'])
def cars():
    conn = database_connection_sqlite()
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
    conn = database_connection_sqlite()
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
