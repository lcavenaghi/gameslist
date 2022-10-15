from flask_restx import fields
from api import api

loja = api.model('loja', {
    '_id': fields.String(required=False, description='Id da loja'),
    'nome': fields.String(required=True, description='Nome da loja'),
    'fundacao': fields.Date(required=True, description='Data de fundação da loja'),
    'link': fields.String(required=True, description='Link da loja')
}, strict=True)
