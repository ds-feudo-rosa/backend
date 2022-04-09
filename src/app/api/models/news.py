from app import db
from flask_login import UserMixin

#criação das tabelas dos usuários, herdando da classe do Model
class NewsModel(db.Model, UserMixin):
    __tablename__ = "news"

    #Criação de Colunas no SQL
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(100), nullable=False, unique=True)

    #Construtor - Inicializa todos os campos, normalmente é os campos obrigatórios, especificando quando ela for inicializada
    def __init__(self, text, title):
        self.text = text
        self.title = title
    
    def get_id(self):
        return str(self.id)
    
    def save(self):
        db.session.add(self)
        return db.session.commit()