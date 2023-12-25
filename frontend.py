from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def main_page():
    user_data = get_user_data()
    return render_template('test.html', user_data=user_data)


def get_user_data():
    return [{"name": "marko", "age": "33", "id": "123153765"}]


if __name__ == '__main__':
    app.run(debug=True, port=80)
