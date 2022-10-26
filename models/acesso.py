from flask_restx import fields
from api import api

acesso = api.model('acesso', {
    'usuario': fields.String(required=True, description='Usuário que acessou'),
    'horario': fields.DateTime(required=True, description='Horário do acesso')
}, strict=True)
