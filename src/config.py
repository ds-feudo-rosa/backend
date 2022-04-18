import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

#Criando a conexão com o Banco de Dados

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'my-precious'