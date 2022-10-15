from flask_restx import fields
from api import api

usuario_update = api.model('usuario_update', {
    '_id': fields.String(required=False, description='Id do usuário'),
    'email': fields.String(required=False, description='Email do usuário'),
    'senha': fields.String(required=False, description='Senha criptografada do usuário'),
    'nome': fields.String(required=False, description='Nome do usuário'),
    'sobrenome': fields.String(required=False, description='Sobrenome do usuário'),
    'tipoDeAcesso': fields.String(required=False, description='Tipo de acesso do usuário')
}, strict=True)