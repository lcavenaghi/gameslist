from controller import ControllerAcessos, ControllerDesenvolvedoras, ControllerJogos, ControllerLojas, ControllerNoticias, ControllerPlataformas, ControllerTags, ControllerUsuarios

class Router():
    def __init__(self, api) -> None:
        self.api = api

    def carregar_rotas(self):
        self.api.add_resource(ControllerAcessos, '/acessos')
        self.api.add_resource(ControllerDesenvolvedoras, '/desenvolvedoras')
        self.api.add_resource(ControllerJogos, '/jogos')
        self.api.add_resource(ControllerLojas, '/lojas')
        self.api.add_resource(ControllerNoticias, '/noticias')
        self.api.add_resource(ControllerPlataformas, '/plataformas')
        self.api.add_resource(ControllerTags, '/tags')
        self.api.add_resource(ControllerUsuarios, '/usuarios')