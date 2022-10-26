from flask_restx import fields
from api import api

usuario = api.model('usuario', {
    '_id': fields.String(required=False, description='Id do usuário'),
    'email': fields.String(required=True, description='Email do usuário'),
    'senha': fields.String(required=True, description='Senha criptografada do usuário'),
    'nome': fields.String(required=True, description='Nome do usuário'),
    'sobrenome': fields.String(required=True, description='Sobrenome do usuário'),
    'tipoDeAcesso': fields.String(required=False, description='Tipo de acesso do usuário')
}, strict=True)
