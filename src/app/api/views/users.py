from flask_restful import Resource
from flask import  request
from app.api.models.users import UserModel
from app import api_restful, bcrypt
from app import db
from flask_login import login_required

class Register(Resource):
    def get(self):
        @login_required
        def logado():
            return 'Usuário Logado', 200
        
        return 'Usuário não está logado', 203
    
    def post(self):
        user =  UserModel(request.form['password'], request.form['name'], request.form['email'])
        if UserModel.query.filter_by(email=user.email).first():
            return 'Nomde de Usuáro e Email já resgistrado'
    
        elif UserModel.query.filter_by(email=user.email).first():
            return 'Email já cadastrado'
        else:
            hash_password = bcrypt.generate_password_hash(user.password)
            new_user = UserModel(password=hash_password, name=user.name, email=user.email)
            new_user.save()
            return 'Cadatro feito com Sucesso', 201

class Login(Resource):
    def get(self):
        @login_required
        def logado():
            return 'Usuário Logado', 200
        
        return 'Usuário não está logado', 203
    
    def post(self):
        user = UserModel.query.filter_by(email=request.form['email']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            return 'Login feito com Sucesso'
        else:
            return 'Dados incorretos'

class EditDelete(Resource):
    def patch(self):
        #Está faltando autenticação e verificador de login
        old_user = UserModel.query.filter_by(email=request.form['email']).first()
        new_user = UserModel(request.form['new_password'], request.form['new_name'], request.form['new_email'])
        old_user = UserModel(name=new_user.name, email=new_user.email, password=new_user.password)
        old_user.save()
        return 'Usuário Editado'
    
    def delete(self):
        user = UserModel.query.filter_by(email=request.form['email']).first()
        db.session.delete(user)
        db.session.commit()
        return 'Usuário Apagado'



class User(Resource):
    def get(self):
        @login_required
        def logado():
            return 'Usuário Logado'
        
        return 'Usuário não está logado', 203


    def post(self):
        return 'Oi'


api_restful.add_resource(Register, '/register/', endpoint='register', methods=['GET', 'POST'])
api_restful.add_resource(Login, '/login/', endpoint='login', methods=['GET', 'POST'])
api_restful.add_resource(EditDelete, '/edit/', endpoint='edit', methods=['PATCH'])
api_restful.add_resource(EditDelete, '/delete/', endpoint='delete', methods=['DELETE'])
api_restful.add_resource(User, '/user/', endpoint='user', methods=['GET', 'POST'])