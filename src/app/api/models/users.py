from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    return UserModel.query.filter_by(id=user_id).first()

#criação das tabelas dos usuários, herdando da classe do Model, e herdando as propriédades de login do UserMixin
class UserModel(db.Model, UserMixin):
    __tablename__ = "users"

    #Criação de Colunas no SQL
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    #Construtor - Inicializa todos os campos, normalmente é os campos obrigatórios, especificando quando ela for inicializada
    def __init__(self, password, name, email):
        self.name = name
        self.email = email
        self.password = password

    #Função de salvamento no banco de dados
    def save(self):
        db.session.add(self)
        return db.session.commit()