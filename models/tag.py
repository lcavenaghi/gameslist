from flask_restx import fields
from api import api

tag = api.model('tag', {
    'nome': fields.String(required=True, description='Descrição da tag')
})