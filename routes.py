from controller import ControllerAcessos, ControllerDesenvolvedora, ControllerDesenvolvedoras, ControllerJogo, ControllerJogos, ControllerLogin
from controller import ControllerLoja, ControllerLojas, ControllerNoticia, ControllerNoticias, ControllerPlataforma, ControllerPlataformas
from controller import ControllerTag, ControllerTags, ControllerUsuario, ControllerUsuarios


class Router():
    def __init__(self, api) -> None:
        self.api = api

    def carregar_rotas(self):
        self.api.add_resource(ControllerAcessos, '/acessos')
        self.api.add_resource(ControllerUsuario, '/usuario/<string:id>')
        self.api.add_resource(ControllerLogin, '/login')        
        self.api.add_resource(ControllerDesenvolvedoras, '/desenvolvedoras')
        self.api.add_resource(ControllerDesenvolvedora,
                              '/desenvolvedora/<string:id>')
        self.api.add_resource(ControllerJogos, '/jogos')
        self.api.add_resource(ControllerJogo, '/jogo/<string:id>')
        self.api.add_resource(ControllerLojas, '/lojas')
        self.api.add_resource(ControllerLoja, '/loja/<string:id>')
        self.api.add_resource(ControllerNoticias, '/noticias')
        self.api.add_resource(ControllerNoticia, '/noticia/<string:id>')
        self.api.add_resource(ControllerPlataformas, '/plataformas')
        self.api.add_resource(ControllerPlataforma, '/plataforma/<string:id>')
        self.api.add_resource(ControllerTags, '/tags')
        self.api.add_resource(ControllerTag, '/tag/<string:id>')
        self.api.add_resource(ControllerUsuarios, '/usuarios')
