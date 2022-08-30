from flask_restx import fields
from api import api

jogo = api.model('jogo', {
    'nome': fields.String(required=True, description='Nome do jogo'),
    'dataLancamento': fields.Date(required=True, description='Data de lançamento do jogo'),
    'descricao': fields.String(required=True, description='Descrição do jogo'),
    'link': fields.String(required=True, description='Link do jogo'),
})