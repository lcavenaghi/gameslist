from flask_restx import fields
from api import api

noticia_update = api.model('noticia_update', {
    '_id': fields.String(required=False, description='Id da noticia'),
    'titulo': fields.String(required=False, description='Título da notícia'),
    'data': fields.Date(required=False, description='Data da publicação da notícia'),
    'resumo': fields.String(required=False, description='Resumo da notícia'),
    'link': fields.String(required=False, description='Link da noticia')
}, strict=True)
