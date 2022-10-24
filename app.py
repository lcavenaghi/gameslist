import logging
import os
from flask import Flask, Blueprint
from api import api
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from routes import Router

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_KEY")
app.config['RESPLUS_VALIDATE'] = True
app.config['RESTPLUS_MASK_SWAGGER'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True

blueprint = Blueprint('api', __name__)
api.init_app(blueprint)
app.register_blueprint(blueprint)
app.wsgi_app = ProxyFix(app.wsgi_app)

routes = Router(api)
routes.carregar_rotas()

if __name__ == '__main__':
    app.logger = logging.getLogger(__name__)
    app.run(debug=True, port=80)
