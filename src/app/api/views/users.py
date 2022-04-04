from flask_restful import Resource
from flask import  request
from app.api.models.users import UserModel
from app import api_restful, bcrypt
from app import db
from flask_login import current_user, login_user, logout_user

class Register(Resource):
    def get(self):
        if current_user.is_authenticated:
            return 'Usuário Logado', 200
        
        return 'Usuário não está logado', 203
    
    def post(self):
        user = UserModel(request.form['password'], request.form['name'], request.form['email'])
        if UserModel.query.filter_by(email=user.email).first():
            return 'Email já resgistrado'
        else:
            hash_password = bcrypt.generate_password_hash(user.password)
            new_user = UserModel(password=hash_password, name=user.name, email=user.email)
            new_user.save()
            return 'Cadatro feito com Sucesso', 201

class Login(Resource):
    def get(self):
        if current_user.is_authenticated:
            return 'Usuário logado {}'.format(current_user.name), 200
        
        return 'Usuário não está logado', 203
    
    def post(self):
        user = UserModel.query.filter_by(email=request.form['email']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            return 'Login feito com sucesso'
        else:
            return 'Dados incorretos'

class Logout(Resource):
    def get(self):
        if current_user.is_authenticated:
            logout_user()
            return 'Logout feito com Sucesso'
        
        else:
            return 'Você não está logado para poder fazer logout'


class EditDelete(Resource):
    def patch(self):
        if current_user.is_authenticated:
            old_user = current_user
            old_user.name = request.form['new_name']
            old_user.email = request.form['new_email']
            old_user.password = bcrypt.generate_password_hash(request.form['new_password'])
            old_user.save()
            return 'Credenciais editadas com sucesso'
            
        else:
            return 'Faça login primeiro antes de editar as credenciais'
    
    def delete(self):
        if current_user.is_authenticated:
            user = current_user
            db.session.delete(user)
            db.session.commit()
            return 'Usuário apagado'

        else:
            return 'Faça login antes de realizar essa ação'

class User(Resource):
    def get(self):
        if current_user.is_authenticated:
            return 'O usuário logado no momento é o {}'.format(current_user.name)
        else:
            return 'Nenhum usuário Logado'


    def post(self):
        return 'Página não encontrada'


api_restful.add_resource(Register, '/register/', endpoint='register', methods=['GET', 'POST'])
api_restful.add_resource(Login, '/login/', endpoint='login', methods=['GET', 'POST'])
api_restful.add_resource(Logout, '/logout/', endpoint='logout', methods=['GET'])
api_restful.add_resource(EditDelete, '/edit/', endpoint='edit', methods=['PATCH'])
api_restful.add_resource(EditDelete, '/delete/', endpoint='delete', methods=['DELETE'])
api_restful.add_resource(User, '/user/', endpoint='user', methods=['GET', 'POST'])