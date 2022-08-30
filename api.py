from flask_restx import Api

api = Api(  version='1.0', 
            title= 'Games List',
            description= 'Games List',
            validate=True,
            security='Bearer Auth'
)
