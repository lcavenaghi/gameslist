from flask_restx import fields
from api import api

jogo_update = api.model('jogo_update', {
    '_id': fields.String(required=False, description='Id do jogo'),
    'nome': fields.String(required=False, description='Nome do jogo'),
    'dataLancamento': fields.Date(required=False, description='Data de lançamento do jogo'),
    'descricao': fields.String(required=False, description='Descrição do jogo'),
    'link': fields.String(required=False, description='Link do jogo'),
}, strict=True)
