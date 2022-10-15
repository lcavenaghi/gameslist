from flask_restx import fields
from api import api

tag_update = api.model('tag_update', {
    '_id': fields.String(required=False, description='Id da noticia'),
    'nome': fields.String(required=False, description='Descrição da tag')
}, strict=True)
