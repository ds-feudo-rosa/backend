from flask import  request
from flask_restful import Resource
from flask_login import current_user
from app import api_restful
from app.api.models.news import NewsModel, VoteModel
import json


'''
Classe destinada a fazer o Registro de Notícias

Método GET - Passos:
    Método Inválido - Para fazer o registro de nóticias é necessário enviar os dados da mesma

Método Post- Passos:
    1 - Vérifica se o Usuário está logado para que possa registrar uma Notícia
        Sim:
            Pega os dados da Notícia por Json
            Verifica se não há nenhuma notícia com texto igual:
            Sim - Retorna que a notícia já foi cadastrada
            Não - Cadastra a Notícia e já cria a parte dos votos
        
        Não - Ação Inválida poís para acessar a página de registrar uma Notícia a pessoa deve está logada

'''

class NewNotice(Resource):
    def get(self):
        return "Ação Invalida"
    
    def post(self):
        if current_user.is_authenticated:
            data = request.get_json()
            if NewsModel.query.filter_by(text=data['text']).first():
                return "Essa noticia já foi cadastrada"
            else:
                notice = NewsModel(title=data['title'], text=data['text'])
                notice.save()
                votos = VoteModel(like=0, unlike=0)
                votos.save()
                return 'Noticia cadastrada com sucesso'
        else:
            return 'Ação Inválida'


'''
Classe destinada a Retornar as Notícias

Método GET - Passos:

Método Post- Passos:
    1 - Recebe o id da Notícia Desejada e verifíca se esse id existe
        Sim - Puxa a Noticia com todos os dados
        Não - Informa que ess Notícia não existe

'''

class ReturnNotice(Resource):
    def get(self):
        noticias = NewsModel.query.all()
        list = []
        for x in noticias:
            dados = x.__dict__
            list.append({ 
                "id": dados['id'],
                "title": dados['title'],
                "text": dados['text']
            })
        return json.dumps(list)        

class ReturnNotice(Resource):
    def get(self):
        noticias = NewsModel.query.all()
        list = []
        for x in noticias:
            dados = x.__dict__
            list.append(dados)

        return json.dumps(list)        

    def post(self):
        data = request.get_json()
        if NewsModel.query.filter_by(id=data['id']).first():
            notice = NewsModel.query.filter_by(id=data['id']).first()
            votos = VoteModel.query.filter_by(id=data['id']).first()
            return json.dumps({
              "title": notice.title, 
              "text": notice.text, 
              "likes": votos.like,
              "unlikes": votos.unlike
            })
        else:
            return 'A notícia com ess id não existe'

'''
Classe destinada para fazer os votos das notícias

Método GET - Passos:

Método Post- Passos:
    1 - Verifíca se o Usuário está logado
    Sim:
        Verifica se exite uma Notícia com aquele id
        Sim - Realiza o voto
        Não - Retorna que não existe aquela notícia
    Não - Ação Inválida, poís o usuário so vai votar quando estiver logado

'''

class VotoNotice(Resource):
    def get(self):
        print('oi')

    def post(self):
        if current_user.is_authenticated:
            data = request.get_json()

            if NewsModel.query.filter_by(id=data['id']).first():
                votos = VoteModel.query.filter_by(id=data['id']).first()
                votos.like = votos.like + int(data['likes'])
                votos.unlike = votos.unlike + int(data['unlikes'])
                votos.save()
                return "Votação Salva"
                
            else:
                return 'Não existe Notícia com esse id'
        else:
            return 'Faça Login antes de votar'


#Criação de Cada rota com referência ao seu endpoit e sua class        

api_restful.add_resource(NewNotice, '/new/', endpoint='news', methods=['GET', 'POST'])
api_restful.add_resource(ReturnNotice, '/notice/', endpoint='notice', methods=['GET', 'POST'])
api_restful.add_resource(VotoNotice, '/voto/', endpoint='voto', methods=['GET', 'POST'])