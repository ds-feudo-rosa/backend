from app import api_restful
from flask_restful import Resource
from flask import  request
from app.api.models.news import NewsModel, VoteModel
from flask_login import current_user

class NewNotice(Resource):
    def get(self):
        return "Ação Invalida"
    
    def post(self):
        if current_user.is_authenticated:
            data = request.get_json()
            notice = NewsModel.query.filter_by(text=data['text']).first()
            if notice:
                return "Essa noticia já foi cadastrada"
            else:
                notice = NewsModel(title=data['title'], text=data['text'])
                notice.save()
                votos = VoteModel(like=0, unlike=0)
                votos.save()
                return 'Noticia cadastrada com sucesso'
        else:
            return 'Faça login antes de publicar uma noticia', 203

class ReturnNotice(Resource):
    def get(self):
        return "Ação Inválida"
    
    def post(self):
        data = request.get_json()
        notice = NewsModel.query.filter_by(id=data['id']).first()
        votos = VoteModel.query.filter_by(id=data['id']).first()
        if notice:
            return ("A noticia é {} Sua quatidade de Votos é {} likes e {} deslikes".format(notice.text, votos.like, votos.unlike))

class VotoNotice(Resource):
    def post(slef):
        if current_user.is_authenticated:
            data = request.get_json()
            notice = NewsModel.query.filter_by(id=data['id']).first()
            if notice:
                votos = VoteModel.query.filter_by(id=data['id']).first()
                votos.like = votos.like + int(data['likes'])
                votos.unlike = votos.unlike + int(data['unlikes'])
                votos.save()
                return "Votação Salva"
    
    def get(self):
        return "Ação Inválida"
        

api_restful.add_resource(NewNotice, '/new/', endpoint='news', methods=['GET', 'POST'])
api_restful.add_resource(ReturnNotice, '/notice/', endpoint='notice', methods=['GET', 'POST'])
api_restful.add_resource(VotoNotice, '/voto/', endpoint='voto', methods=['GET', 'POST'])