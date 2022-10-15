from flask_restx import fields
from api import api

plataforma_update = api.model('plataforma_update', {
    '_id': fields.String(required=False, description='Id da plataforma'),
    'nome': fields.String(required=False, description='Nome da plataforma'),
    'dataDeLancamento': fields.Date(required=False, description='Data de lançamento da plataforma')
}, strict=True)
