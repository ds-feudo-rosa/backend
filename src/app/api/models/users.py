from app import db
from flask_login import UserMixin

#criação das tabelas dos usuários, herdando da classe do Model
class UserModel(db.Model, UserMixin):
    __tablename__ = "users"

    #Criação de Colunas no SQL
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(15))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

    #Construtor - Inicializa todos os campos, normalmente é os campos obrigatórios, especificando quando ela for inicializada
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
    
    #Decorator de propriédades de login
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
    
    def save(self):
        db.session.add(self)
        return db.session.commit()