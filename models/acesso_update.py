from flask_restx import fields
from api import api

acesso_update = api.model('acesso_update', {
    '_id': fields.String(required=False, description='Id do acesso'),
    'usuario': fields.String(required=False, description='Usuário que acessou'),
    'horario': fields.DateTime(required=False, description='Horário do acesso')
}, strict=True)
