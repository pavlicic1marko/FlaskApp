import requests
from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')
from forms import RegistrationForm, LoginForm

# protect against cookie modification, csrf tokens
app.config['SECRET_KEY'] = 'v34erjlb8o37444rrrr934gfriyf3'

random_microservice_url = "http://127.0.0.1:5000"


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def main_page():
    user_data = get_user_data()
    return render_template('test.html', user_data=user_data, title='BEST')


@app.route('/about', methods=['GET'])
def about_page():
    user_data = get_user_data()
    return render_template('about.html', user_data=user_data, title='BEST')


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', titl='Register', form=form)


@app.route('/login')
def login():
    pass
    #form = RegistrationForm()
    #return render_template('login.html', titl='Login', form=form)


def get_user_data():
    response = requests.get(random_microservice_url)
    return response.json()


if __name__ == '__main__':
    app.run(debug=True, port=80)
