from flask_restful import Resource, Api
from flask import Blueprint, request
from flask_cors import CORS

user_blueprint = Blueprint('user_view', __name__)
api = Api(user_blueprint)
CORS(user_blueprint)

class User(Resource):
    def get(self):
        return 'Helo World!', 200

api.add_resource(User, '/api/user/', endpoint='user', methods=['GET'] )