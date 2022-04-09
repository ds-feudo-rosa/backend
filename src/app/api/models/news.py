from app import db

#criação das tabelas dos usuários, herdando da classe do Model
class NewsModel(db.Model):
    __tablename__ = "news"

    #Criação de Colunas no SQL
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False, unique=False)
    text = db.Column(db.String(), nullable=False, unique=False)

    #Construtor - Inicializa todos os campos, normalmente é os campos obrigatórios, especificando quando ela for inicializada
    def __init__(self, title, text):
        self.title = title
        self.text = text
    
    def get_id(self):
        return str(self.id)
    
    def save(self):
        db.session.add(self)
        return db.session.commit()

class VoteModel(db.Model):
    __tablename__ = "vote"

    #Criação de Colunas no SQL
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    like = db.Column(db.Integer)
    unlike = db.Column(db.Integer)

    #Construtor - Inicializa todos os campos, normalmente é os campos obrigatórios, especificando quando ela for inicializada
    def __init__(self, like, unlike):
        self.like = like
        self.unlike = unlike
    
    def get_id(self):
        return str(self.id)
    
    def save(self):
        db.session.add(self)
        return db.session.commit()