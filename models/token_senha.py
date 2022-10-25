from flask_restx import fields
from api import api

token_senha = api.model('token_senha', {
    'token': fields.String(required=True, description='Token para reset de senha do usuário'),
    'senha': fields.String(required=True, description='Nova senha do usuário')
}, strict=True)
