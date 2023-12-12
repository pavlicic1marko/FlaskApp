from flask import Flask, jsonify, render_template, request
from markupsafe import escape
import random


app = Flask(__name__, template_folder='templates')

users = {"users": [{"name": "marko", "age": 12}, {"name": "wewe", "age": 132}]}
car_list =[
    {
    "id":0,
    "model":"BMW-RT",
    "price":"10"
     },

    {
    "id":1,
    "model":"BMW-XC",
    "price":"20"
    }
]

@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    #note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route("/users")
def users():
    return jsonify({"users": [{"name": "marko", "age": 12}, {"name": "wewe", "age": 132}]})


@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/test')
def test():
    return jsonify({"users": "testss"})

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/cars', methods=['GET','POST'])
def cars():
    if request.method == 'GET':
        if len(car_list)>0:
            return jsonify(car_list)
        else:
            return 'no cars found', 404

    if request.method == 'POST':
        new_id = random.randint(1000, 2000)
        new_model = request.form['model']
        new_price = request.form['price']

        new_obj = {
            'id': new_id,
            'model': new_model,
            'price': new_price
        }
        car_list.append(new_obj)
        return jsonify(car_list),201







if __name__ == '__main__':
    app.run(debug=True, port=80)
