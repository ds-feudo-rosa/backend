from app import db

#criação das tabelas dos usuários, herdando da classe do Model
class UserModel(db.Model):
    __tablename__ = "users"

    #Criação de Colunas no SQL
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    #Construtor - Inicializa todos os campos, normalmente é os campos obrigatórios, especificando quando ela for inicializada
    def __init__(self, password, name, email):
        self.name = name
        self.email = email
        self.password = password
    
    def get_id(self):
        return str(self.id)
    
    def save(self):
        db.session.add(self)
        return db.session.commit()