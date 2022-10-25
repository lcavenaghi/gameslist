from flask_restx import Resource
from api import api
from common.jwt import requer_jwt
from flask_jwt_extended import get_jwt_identity

from models.usuario import usuario
from models.usuario_update import usuario_update
from models.tag import tag
from models.tag_update import tag_update
from models.plataforma import plataforma
from models.plataforma_update import plataforma_update
from models.noticia import noticia
from models.noticia_update import noticia_update
from models.loja import loja
from models.loja_update import loja_update
from models.jogo import jogo
from models.jogo_update import jogo_update
from models.desenvolvedora import desenvolvedora
from models.desenvolvedora_update import desenvolvedora_update
from models.acesso import acesso
from models.login_model import login_model
from models.esqueci_senha import esqueci_senha
from models.token_senha import token_senha

from common.mongo_db import MongoDb
from common.auth import Auth
mongo_db = MongoDb()
auth = Auth()


class ControllerAcessos(Resource):
    collection = "acessos"

    @requer_jwt()
    @api.marshal_list_with(acesso)
    def get(self):
        return mongo_db.db_find(self.collection, True, {"email": get_jwt_identity()})


class ControllerDesenvolvedoras(Resource):
    collection = "desenvolvedoras"

    @requer_jwt()
    @api.marshal_list_with(desenvolvedora)
    def get(self):
        return mongo_db.get_all(self.collection)

    @requer_jwt()
    @api.expect(desenvolvedora)
    @api.marshal_with(desenvolvedora, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerDesenvolvedora(Resource):
    collection = "desenvolvedoras"

    @requer_jwt()
    @api.marshal_list_with(desenvolvedora)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @requer_jwt()
    @api.marshal_with(desenvolvedora, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @requer_jwt()
    @api.expect(desenvolvedora_update)
    @api.marshal_with(desenvolvedora, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerJogos(Resource):
    collection = "jogos"

    @requer_jwt()
    @api.marshal_list_with(jogo)
    def get(self):
        return mongo_db.get_all(self.collection)

    @requer_jwt()
    @api.expect(jogo)
    @api.marshal_with(jogo, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerJogo(Resource):
    collection = "jogos"

    @requer_jwt()
    @api.marshal_list_with(jogo)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @requer_jwt()
    @api.marshal_with(jogo, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @requer_jwt()
    @api.expect(jogo_update)
    @api.marshal_with(jogo, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerLojas(Resource):
    collection = "lojas"

    @requer_jwt()
    @api.marshal_list_with(loja)
    def get(self):
        return mongo_db.get_all(self.collection)

    @requer_jwt()
    @api.expect(loja)
    @api.marshal_with(loja, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerLoja(Resource):
    collection = "lojas"

    @requer_jwt()
    @api.marshal_list_with(loja)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @requer_jwt()
    @api.marshal_with(loja, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @requer_jwt()
    @api.expect(loja_update)
    @api.marshal_with(loja, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerNoticias(Resource):
    collection = "noticias"

    @requer_jwt()
    @api.marshal_list_with(noticia)
    def get(self):
        return mongo_db.get_all(self.collection)

    @requer_jwt(["gestor"])
    @api.expect(noticia)
    @api.marshal_with(noticia, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerNoticia(Resource):
    collection = "noticias"

    @requer_jwt()
    @api.marshal_list_with(noticia)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @requer_jwt(["gestor"])
    @api.marshal_with(noticia, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @requer_jwt(["gestor"])
    @api.expect(noticia_update)
    @api.marshal_with(noticia, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerPlataformas(Resource):
    collection = "plataformas"

    @requer_jwt()
    @api.marshal_list_with(plataforma)
    def get(self):
        return mongo_db.get_all(self.collection)

    @requer_jwt(["gestor"])
    @api.expect(plataforma)
    @api.marshal_with(plataforma, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerPlataforma(Resource):
    collection = "plataformas"

    @requer_jwt()
    @api.marshal_list_with(plataforma)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @requer_jwt(["gestor"])
    @api.marshal_with(plataforma, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @requer_jwt(["gestor"])
    @api.expect(plataforma_update)
    @api.marshal_with(plataforma, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerTags(Resource):
    collection = "tags"

    @requer_jwt()
    @api.marshal_list_with(tag)
    def get(self):
        return mongo_db.get_all(self.collection)

    @requer_jwt(["gestor"])
    @api.expect(tag)
    @api.marshal_with(tag, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerTag(Resource):
    collection = "tags"

    @requer_jwt()
    @api.marshal_list_with(tag)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @requer_jwt(["gestor"])
    @api.marshal_with(tag, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @requer_jwt(["gestor"])
    @api.expect(tag_update)
    @api.marshal_with(tag, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerUsuarios(Resource):
    collection = "usuarios"

    @requer_jwt(["admin"])
    @api.marshal_list_with(usuario)
    def get(self):
        return mongo_db.get_all(self.collection)

    @api.expect(usuario)
    @api.marshal_with(usuario, code=201)
    def post(self):
        return auth.registra(api.payload)


class ControllerUsuario(Resource):
    collection = "usuarios"

    @requer_jwt(["admin"])
    @api.marshal_list_with(usuario)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @requer_jwt(["admin"])
    @api.marshal_with(usuario, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @requer_jwt(["admin"])
    @api.expect(usuario_update)
    @api.marshal_with(usuario, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerLogin(Resource):
    @api.expect(login_model)
    def post(self):
        return auth.processa_login(api.payload["email"], api.payload["senha"])


class ControllerEsqueciSenha(Resource):
    @api.expect(esqueci_senha)
    def post(self):
        return auth.envia_email_esqueci_senha(api.payload["email"])
    
    @api.expect(token_senha)
    def patch(self):
        return auth.altera_senha(api.payload["token"], api.payload["senha"])
