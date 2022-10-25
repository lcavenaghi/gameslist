from flask_restx import fields
from api import api

esqueci_senha = api.model('esqueci_senha', {
    'email': fields.String(required=True, description='Login do usuário')
}, strict=True)
