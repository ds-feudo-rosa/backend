from flask_restful import Resource, Api
from flask import Blueprint, request
from flask_cors import CORS
from app.api.models.users import UserModel
#from app import bcrypt

user_blueprint = Blueprint('user_view', __name__)
api = Api(user_blueprint)
CORS(user_blueprint)

class User(Resource):
    def get(self):
        return 'Helo World!', 200

    def post(self):
        i = UserModel(request.form['username'], request.form['password'], request.form['name'], request.form['email'])
        if UserModel.query.filter_by(username=i.username).first():
            if UserModel.query.filter_by(email=i.email).first():
                return 'Nomde de Usuáro e Email já resgistrado'
            return 'Nomde de Usuáro já resgistrado'
    
        elif UserModel.query.filter_by(email=i.email).first():
            return 'Email já cadastrado'
        else:
            #hash_password = bcrypt.generate_password_hash(i.password)
            new_user = UserModel(username=i.username, password=i.password, name=i.name, email=i.email)
            new_user.save()
            return 'Cadatro feito com Sucesso'

api.add_resource(User, '/api/user/', endpoint='user', methods=['GET', 'POST'] )