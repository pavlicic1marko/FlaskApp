from flask import Blueprint, jsonify

user_blueprint = Blueprint('user_api_routes', __name__, url_prefix='/api/users')


@user_blueprint.route('/')
def index():
    return jsonify({"users": ""})

