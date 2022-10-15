from flask_restx import fields
from api import api

loja_update = api.model('loja_update', {
    '_id': fields.String(required=False, description='Id da loja'),
    'nome': fields.String(required=False, description='Nome da loja'),
    'fundacao': fields.Date(required=False, description='Data de fundação da loja'),
    'link': fields.String(required=False, description='Link da loja')
}, strict=True)
