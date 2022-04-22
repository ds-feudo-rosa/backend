from app import db

#criação das tabelas de Notícias, herdando da classe do Model
class NewsModel(db.Model):
    __tablename__ = "news"

    #Criação de Colunas no SQL
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False, unique=False)
    text = db.Column(db.String(), nullable=False, unique=True)
    url = db.Column(db.String(), nullable=True, unique=False)

    #Construtor - Inicializa todos os campos, normalmente é os campos obrigatórios, especificando quando ela for inicializada
    def __init__(self, title, text, url=""):
        self.title = title
        self.text = text
        self.url = url
    
    #Função de salvamento no banco de dados
    def save(self):
        db.session.add(self)
        return db.session.commit()


#criação das tabelas de Votos, herdando da classe do Model
class VoteModel(db.Model):
    __tablename__ = "vote"

    #Criação de Colunas no SQL
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    like = db.Column(db.Integer, nullable=True)
    unlike = db.Column(db.Integer, nullable=True)

    #Construtor - Inicializa todos os campos, normalmente é os campos obrigatórios, especificando quando ela for inicializada
    def __init__(self, like, unlike):
        self.like = like
        self.unlike = unlike
    
    #Função de salvamento no banco de dados
    def save(self):
        db.session.add(self)
        return db.session.commit()