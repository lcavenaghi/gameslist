from flask_restx import Resource
from api import api

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
from models.acesso_update import acesso_update
from models.login_model import login_model

from common.mongo_db import MongoDb
from common.auth import Auth
mongo_db = MongoDb()
auth = Auth()


class ControllerAcessos(Resource):
    collection = "acessos"

    @api.marshal_list_with(acesso)
    def get(self):
        return mongo_db.get_all(self.collection)

    @api.expect(acesso)
    @api.marshal_with(acesso, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerAcesso(Resource):
    collection = "acessos"

    @api.marshal_list_with(acesso)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @api.marshal_with(acesso, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @api.expect(acesso_update)
    @api.marshal_with(acesso, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerDesenvolvedoras(Resource):
    collection = "desenvolvedoras"

    @api.marshal_list_with(desenvolvedora)
    def get(self):
        return mongo_db.get_all(self.collection)

    @api.expect(desenvolvedora)
    @api.marshal_with(desenvolvedora, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerDesenvolvedora(Resource):
    collection = "desenvolvedoras"

    @api.marshal_list_with(desenvolvedora)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @api.marshal_with(desenvolvedora, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @api.expect(desenvolvedora_update)
    @api.marshal_with(desenvolvedora, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerJogos(Resource):
    collection = "jogos"

    @api.marshal_list_with(jogo)
    def get(self):
        return mongo_db.get_all(self.collection)

    @api.expect(jogo)
    @api.marshal_with(jogo, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerJogo(Resource):
    collection = "jogos"

    @api.marshal_list_with(jogo)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @api.marshal_with(jogo, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @api.expect(jogo_update)
    @api.marshal_with(jogo, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerLojas(Resource):
    collection = "lojas"

    @api.marshal_list_with(loja)
    def get(self):
        return mongo_db.get_all(self.collection)

    @api.expect(loja)
    @api.marshal_with(loja, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerLoja(Resource):
    collection = "lojas"

    @api.marshal_list_with(loja)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @api.marshal_with(loja, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @api.expect(loja_update)
    @api.marshal_with(loja, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerNoticias(Resource):
    collection = "noticias"

    @api.marshal_list_with(noticia)
    def get(self):
        return mongo_db.get_all(self.collection)

    @api.expect(noticia)
    @api.marshal_with(noticia, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerNoticia(Resource):
    collection = "noticias"

    @api.marshal_list_with(noticia)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @api.marshal_with(noticia, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @api.expect(noticia_update)
    @api.marshal_with(noticia, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerPlataformas(Resource):
    collection = "plataformas"

    @api.marshal_list_with(plataforma)
    def get(self):
        return mongo_db.get_all(self.collection)

    @api.expect(plataforma)
    @api.marshal_with(plataforma, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerPlataforma(Resource):
    collection = "plataformas"

    @api.marshal_list_with(plataforma)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @api.marshal_with(plataforma, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @api.expect(plataforma_update)
    @api.marshal_with(plataforma, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerTags(Resource):
    collection = "tags"

    @api.marshal_list_with(tag)
    def get(self):
        return mongo_db.get_all(self.collection)

    @api.expect(tag)
    @api.marshal_with(tag, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerTag(Resource):
    collection = "tags"

    @api.marshal_list_with(tag)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @api.marshal_with(tag, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @api.expect(tag_update)
    @api.marshal_with(tag, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)


class ControllerUsuarios(Resource):
    collection = "usuarios"

    @api.marshal_list_with(usuario)
    def get(self):
        return mongo_db.get_all(self.collection)

    @api.expect(usuario)
    @api.marshal_with(usuario, code=201)
    def post(self):
        return mongo_db.insert(self.collection, api.payload)


class ControllerUsuario(Resource):
    collection = "usuarios"

    @api.marshal_list_with(usuario)
    def get(self, id):
        return mongo_db.get(self.collection, id)

    @api.marshal_with(usuario, code=201)
    def delete(self, id):
        return mongo_db.delete(self.collection, id)

    @api.expect(usuario_update)
    @api.marshal_with(usuario, code=201)
    def patch(self, id):
        return mongo_db.patch(self.collection, id, api.payload)

class ControllerLogin(Resource):
    @api.expect(login_model)
    def post(self):
        return auth.process_login_request(api.payload["email"], api.payload["senha"])
