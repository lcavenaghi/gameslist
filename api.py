from flask_restx import Api

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Para utilizar, colocar o jwt: 'Bearer [jwt]'"
    }
}

api = Api(version='1.0',
          title='Games List',
          description='Games List',
          validate=True,
          security='Bearer Auth',
          authorizations=authorizations
          )
