from flask_restx import fields
from api import api

desenvolvedora_update = api.model('desenvolvedora_update', {
    '_id': fields.String(required=False, description='Id da desenvolvedora'),
    'nome': fields.String(required=False, description='Nome da desenvolvedora'),
    'fundacao': fields.Date(required=False, description='Data de fundação da desenvolvedora'),
    'localizacao': fields.String(required=False, description='Localização da desenvolvedora')
}, strict=True)
