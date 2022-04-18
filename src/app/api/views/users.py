from flask import  request
from flask_restful import Resource
from flask_login import current_user, login_user, logout_user
from app import db
from app import api_restful, bcrypt
from app.api.models.users import UserModel


'''
Classe destinada a fazer o cadastro de usuários

Método GET - Passos:
    1 - Verificar se o usuário está logado:
        Sim - Mandar ele para a página de perfil, poís ele não precisa fazer outro registro
        Não - Mandar ele para a página de registro

Método POST - Passos:
    1 - Verificar se o usuário está logado:
        Sim - Mandar ele para a página de perfil, poís ele não precisa fazer outro registro
        Não:
            Pega os dados através de um Json
            Verifica se o e-mail já existe no banco de dados:
                Sim - Retorna uma mensagem de E-mail inválido
                Não - Realiza o cadastro
'''

class Register(Resource):
    def get(self):
        if current_user.is_authenticated:
            return 'Já existe um usuário logado, o {}'.format(current_user.name)
        
        return 'Redirecionamento para a página de Registro de Usuários'
    
    def post(self):
        if current_user.is_authenticated:
            return 'Já existe um usuário logado, o {}'.format(current_user.name)
        else:
            data = request.get_json()
            if UserModel.query.filter_by(email=data['email'].lower()).first():
                return 'Email já resgistrado'
            else:
                hash_password = bcrypt.generate_password_hash(data['password'])
                new_user = UserModel(name=data['name'], email=data['email'].lower(), password=hash_password)
                new_user.save()
                logout_user()
                return 'Cadatro feito com Sucesso'


'''
Classe destinada a fazer o Login de usuários

Método GET - Passos:
    1 - Verificar se o usuário está logado:
        Sim - Mostra os dados do Usuário
        Não - Redireciona para a página de login

Método POST - Passos:
    1 - Verificar se o usuário está logado:
        Sim - Ação invalida poís não tem como o usuário ver o formulário já que já está logado
        Não - Vérifica se os dados estão corretos e se sim realiza o lgin.
'''

class Login(Resource):
    def get(self):
        if current_user.is_authenticated:
            return 'Usuário logado {}'.format(current_user.name)
        
        return 'Redirecionamento para o login'
    
    def post(self):
        if current_user.is_authenticated:
            return "Usuário {} já logado".format(current_user.name)
        else:
            data = request.get_json()
            user = UserModel.query.filter_by(email=data['email'].lower()).first()
            if user and bcrypt.check_password_hash(user.password, data['password']):
                login_user(user)
                return 'Login do usuário {}'.format(current_user.name)
            else:
                return 'Dados incorretos'


'''
Classe destinada a fazer Logout de usuários

Método GET - Passos:
    1 - Verificar se o usuário está logado:
        Sim - Faz o Logout
        Não - Ação inválida, poís ele precisa está logado para fazer o login
'''

class Logout(Resource):
    def get(self):
        if current_user.is_authenticated:
            logout_user()
            return 'Logout feito'
        
        else:
            return 'Ação Inválida'


'''
Classe destinada a fazer a Edição de dados de usuários e Deletar usuários

Método PATH - Passos:
    1 - Verificar se o usuário está logado:
        Sim:
            Pega os novos dados que serão passados pelo Json
            Substitui os dados antigos
            Salva as alterações
        Não - Redireciona para a página de login

Método DELETE - Passos:
    1 - Verificar se o usuário está logado:
        Sim - Delte o Usuário
        Não - Ação invalida, poís para fazer o delete é necessário está logado
'''

class EditDelete(Resource):
    def patch(self):
        if current_user.is_authenticated:
            data = request.get_json()
            if UserModel.query.filter_by(email=data['new_email'].lower()).first():
                return 'Esse e-mail já existe'
            
            else:
                current_user.name = data['new_name']
                current_user.email = data['new_email']
                current_user.password = bcrypt.generate_password_hash(data['new_password'])
                current_user.save()
                return 'Credenciais editadas'
        else:
            return 'Ação Inválida'
    
    def delete(self):
        if current_user.is_authenticated:
            db.session.delete(current_user)
            db.session.commit()
            return 'Usuário apagado'

        else:
            return 'Ação Inválida'

'''
Classe destinada a fazer Puxar as informações de Usuário

Método GET - Passos:
    1 - Verificar se o usuário está logado:
        Sim:
            Retorna os dados do usuário
        Não - Ação Inválida

Método Post- Passos:
    Método Inválido
'''

class User(Resource):
    def get(self):
        if current_user.is_authenticated:
            return 'O usuário logado {}'.format(current_user.name)
        else:
            return 'Ação Inválida'


    def post(self):
        return 'Método Inválido'

#Criação de Cada rota com referência ao seu endpoit e sua class

api_restful.add_resource(Register, '/register/', endpoint='register', methods=['GET', 'POST'])
api_restful.add_resource(Login, '/login/', endpoint='login', methods=['GET', 'POST'])
api_restful.add_resource(Logout, '/logout/', endpoint='logout', methods=['GET'])
api_restful.add_resource(EditDelete, '/edit/', endpoint='edit', methods=['PATCH'])
api_restful.add_resource(EditDelete, '/delete/', endpoint='delete', methods=['DELETE'])
api_restful.add_resource(User, '/user/', endpoint='user', methods=['GET', 'POST'])