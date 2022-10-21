import logging
from flask import Flask, Blueprint
from api import api
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS

from routes import Router

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
blueprint = Blueprint('api', __name__)

api.init_app(blueprint)
app.register_blueprint(blueprint)
app.wsgi_app = ProxyFix(app.wsgi_app)

routes = Router(api)
routes.carregar_rotas()

if __name__ == '__main__':
    app.logger= logging.getLogger(__name__)
    app.run(debug=True, port=80)