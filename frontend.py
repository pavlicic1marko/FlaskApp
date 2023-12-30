import requests
from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from forms import RegistrationForm, LoginForm, News

app = Flask(__name__, template_folder='templates')

# protect against cookie modification, csrf tokens
app.config['SECRET_KEY'] = 'v34erjlb8o37444rrrr934gfriyf3'

random_microservice_url = "http://127.0.0.1:5000"
backend = "http://127.0.0.1:5000/api/notifications"


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    user_data = get_user_data()
    return render_template('home.html', user_data=user_data, title='BEST')


@app.route('/notifications', methods=['GET', 'POST'])
def news():
    form = News()
    if request.method == 'POST':
        title = form.title.data
        text = form.text.data
        response = requests.post(backend, data={"title": title, "text": text})
        return render_template('notifications.html', notifications_data=response.json(), title='Notifications', form=form)


    if request.method == 'GET':

        notifications_list = get_notifications_list()
        return render_template('notifications.html', notifications_data=notifications_list, title='Notifications', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', titl='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@test.com':
            flash('You are now logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Wrong password or email', 'danger')
    return render_template('login.html', titl='Login', form=form)


def get_user_data():
    response = requests.get(random_microservice_url)
    return response.json()

def get_notifications_list():
    response = requests.get(backend)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True, port=80)
