from flask_restx import Api
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(  version='1.0', 
            title= 'Games List',
            description= 'Games List',
            validate=True,
            security='Bearer Auth',
            authorizations=authorizations,
)
