from flask_restx import Resource
from api import api

from models.acesso import acesso
from models.desenvolvedora import desenvolvedora
from models.jogo import jogo
from models.loja import loja
from models.noticia import noticia
from models.plataforma import plataforma
from models.tag import tag
from models.usuario import usuario

class ControllerUsuarios(Resource):
    @api.marshal_list_with(usuario)
    def get(self):
        return 'todo', 200

    @api.expect(usuario)
    @api.marshal_with(usuario, code=201)
    def post(self):
        return 'todo', 201
    
    @api.expect(usuario)
    @api.marshal_with(usuario, code=201)
    def delete(self):
        return 'todo', 200
        
    @api.expect(usuario)
    @api.marshal_with(usuario, code=201)
    def patch(self):
        return 'todo', 200

class ControllerAcessos(Resource):
    @api.marshal_list_with(acesso)
    def get(self):
        return 'todo', 200

    @api.expect(acesso)
    @api.marshal_with(acesso, code=201)
    def post(self):
        return 'todo', 201
    
    @api.expect(acesso)
    @api.marshal_with(acesso, code=201)
    def delete(self):
        return 'todo', 200
        
    @api.expect(acesso)
    @api.marshal_with(acesso, code=201)
    def patch(self):
        return 'todo', 200

class ControllerDesenvolvedoras(Resource):
    @api.marshal_list_with(desenvolvedora)
    def get(self):
        return 'todo', 200

    @api.expect(desenvolvedora)
    @api.marshal_with(desenvolvedora, code=201)
    def post(self):
        return 'todo', 201
    
    @api.expect(desenvolvedora)
    @api.marshal_with(desenvolvedora, code=201)
    def delete(self):
        return 'todo', 200
        
    @api.expect(desenvolvedora)
    @api.marshal_with(desenvolvedora, code=201)
    def patch(self):
        return 'todo', 200

class ControllerJogos(Resource):
    @api.marshal_list_with(jogo)
    def get(self):
        return 'todo', 200

    @api.expect(jogo)
    @api.marshal_with(jogo, code=201)
    def post(self):
        return 'todo', 201
    
    @api.expect(jogo)
    @api.marshal_with(jogo, code=201)
    def delete(self):
        return 'todo', 200
        
    @api.expect(jogo)
    @api.marshal_with(jogo, code=201)
    def patch(self):
        return 'todo', 200

class ControllerLojas(Resource):
    @api.marshal_list_with(loja)
    def get(self):
        return 'todo', 200

    @api.expect(loja)
    @api.marshal_with(loja, code=201)
    def post(self):
        return 'todo', 201
    
    @api.expect(loja)
    @api.marshal_with(loja, code=201)
    def delete(self):
        return 'todo', 200
        
    @api.expect(loja)
    @api.marshal_with(loja, code=201)
    def patch(self):
        return 'todo', 200

class ControllerNoticias(Resource):
    @api.marshal_list_with(noticia)
    def get(self):
        return 'todo', 200

    @api.expect(noticia)
    @api.marshal_with(noticia, code=201)
    def post(self):
        return 'todo', 201
    
    @api.expect(noticia)
    @api.marshal_with(noticia, code=201)
    def delete(self):
        return 'todo', 200
        
    @api.expect(noticia)
    @api.marshal_with(noticia, code=201)
    def patch(self):
        return 'todo', 200

class ControllerPlataformas(Resource):
    @api.marshal_list_with(plataforma)
    def get(self):
        return 'todo', 200

    @api.expect(plataforma)
    @api.marshal_with(plataforma, code=201)
    def post(self):
        return 'todo', 201
    
    @api.expect(plataforma)
    @api.marshal_with(plataforma, code=201)
    def delete(self):
        return 'todo', 200
        
    @api.expect(plataforma)
    @api.marshal_with(plataforma, code=201)
    def patch(self):
        return 'todo', 200

class ControllerTags(Resource):
    @api.marshal_list_with(tag)
    def get(self):
        return 'todo', 200

    @api.expect(tag)
    @api.marshal_with(tag, code=201)
    def post(self):
        return 'todo', 201
    
    @api.expect(tag)
    @api.marshal_with(tag, code=201)
    def delete(self):
        return 'todo', 200
        
    @api.expect(tag)
    @api.marshal_with(tag, code=201)
    def patch(self):
        return 'todo', 200