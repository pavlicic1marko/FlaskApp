from flask import Flask, jsonify
import requests
from urllib3.exceptions import NewConnectionError

app = Flask(__name__)

random_microservice_url = "http://127.0.0.1:5001/"


# Calling the random number generator microservice
def call_random_microservie():
    response = requests.get(random_microservice_url)
    return response.json().get("random_number")



@app.route("/", methods=['GET'])
def check_even_odd():
    try:
        random_number = call_random_microservie()
    except requests.exceptions.ConnectionError  as e:
        return jsonify({"random_number": 'there is an  connection error'})

    result = "even" if random_number % 2 == 0 else "odd"
    return jsonify({"random_number": random_number, "result": result})


if __name__ == "__main__":
    app.run(port=5000)
