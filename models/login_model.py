from flask_restx import fields
from api import api

login_model = api.model('login_model', {
    'email': fields.String(required=True, description='Login do usuário'),
    'senha': fields.String(required=True, description='Senha criptografada do usuário')
}, strict=True)
