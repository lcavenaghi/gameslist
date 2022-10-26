from flask_restx import fields
from api import api

token_google = api.model('token_google', {
    'token': fields.String(required=True, description='Token do google')
}, strict=True)
