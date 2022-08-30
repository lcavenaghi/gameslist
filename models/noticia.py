from flask_restx import fields
from api import api

noticia = api.model('noticia', {
    'titulo': fields.String(required=True, description='Título da notícia'),
    'data': fields.Date(required=True, description='Data da publicação da notícia'),
    'resumo': fields.String(required=True, description='Resumo da notícia'),
    'link': fields.String(required=True, description='Link da noticia')
})