from flask_restx import fields
from api import api

plataforma = api.model('plataforma', {
    '_id': fields.String(required=False, description='Id da plataforma'),
    'nome': fields.String(required=True, description='Nome da plataforma'),
    'dataDeLancamento': fields.Date(required=True, description='Data de lançamento da plataforma')
}, strict=True)
