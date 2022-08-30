import logging
from flask import Flask, Blueprint
from api import api
from werkzeug.middleware.proxy_fix import ProxyFix

from routes import Router

app = Flask(__name__)
blueprint = Blueprint('api', __name__)

api.init_app(blueprint)
app.register_blueprint(blueprint)
app.wsgi_app = ProxyFix(app.wsgi_app)

routes = Router(api)
routes.carregar_rotas()

if __name__ == '__main__':
    app.logger= logging.getLogger(__name__)
    app.run(debug=True, port=5000)