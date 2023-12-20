import random
from flask import Flask, jsonify, render_template, request
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


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/cars', methods=['GET', 'POST'])
def test():
    conn = database_connection_postgresql()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM cars")
        results = cursor.fetchall() #TODO, if len()== 0 return 'there are no cars'
        cursor.close()
        conn.close()
        return results, 200

    if request.method == 'POST':
        new_model = request.form['model']
        new_price = request.form['price']
        cursor.execute("""INSERT INTO cars (id,model, price) VALUES (%s, %s, %s)""",
                       (random.randint(100000000, 900000000), new_model, new_price,))
        conn.commit()
        cursor.execute("SELECT * FROM cars") #TODO, Get created car
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results, 201


@app.route('/cars/<int:car_id>', methods=['GET', 'PUT', 'DELETE'])
def test_get_one_car(car_id):
    conn = database_connection_postgresql()
    cursor = conn.cursor()
    if request.method == 'DELETE':
        cursor.execute("""DELETE FROM cars WHERE id= %s""", (car_id,))
        conn.commit()
        cursor.execute("SELECT * FROM cars")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results

    if request.method == 'GET':
        cursor.execute("""SELECT * FROM cars WHERE id = %s""", (car_id,))
        results = cursor.fetchall() #TODO if len()==0 return 'no results'
        cursor.close()
        conn.close()
        return results, 200

    if request.method == 'PUT':
        new_model = request.form['model']
        new_price = request.form['price']
        cursor.execute("""UPDATE cars SET model=%s, price=%s WHERE id=%s""", (new_model, new_price, car_id))
        conn.commit()
        cursor.execute("SELECT * FROM cars") #TODO get car by id
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results








if __name__ == '__main__':
    app.run(debug=True, port=80)
