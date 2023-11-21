from flask import Flask, jsonify, render_template
from markupsafe import escape


app = Flask(__name__, template_folder='templates')

users = {"users": [{"name": "marko", "age": 12}, {"name": "wewe", "age": 132}]}


@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route("/users")
def users():
    return jsonify({"users": [{"name": "marko", "age": 12}, {"name": "wewe", "age": 132}]})


@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


if __name__ == '__main__':
    app.run(debug=True, port=5001)
