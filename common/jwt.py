from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps

def requer_jwt(tipo_de_acesso=["usuario", "admin", "gestor"]):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if(claims["tipoDeAcesso"] in tipo_de_acesso):
                return fn(*args, **kwargs)
            else:
                return {"errorMessage": "Sem permissão de acesso"}
        return decorator
    return wrapper