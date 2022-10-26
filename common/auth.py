from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from common.email import get_message, send_mail
from common.mongo_db import MongoDb
import os
import jwt
import bcrypt
from google.oauth2 import id_token
from google.auth.transport import requests

load_dotenv()


class Auth():
    def __init__(self):
        self.mongo_db = MongoDb()

    def processa_login(self, email, senha):
        user = self.mongo_db.db_find("usuarios", False, {"email": email})[0]
        if not user or "senha" not in user:
            return {"errorMessage": "Usuario nao encontrado."}, 401

        if not self.check_password(senha, user["senha"]):
            return {"errorMessage": "Senha invalida."}, 401

        access_token = self.encode_jwt(
            user["email"], user["tipoDeAcesso"])

        self.mongo_db.insert(
            "acessos", {"usuario": user["email"], "horario": datetime.utcnow()})

        return {"token": access_token}, 200

    def processa_login_google(self, token):
        try:
            idinfo = id_token.verify_oauth2_token(
                token, requests.Request(), os.getenv("GOOGLE_CLIENT_ID"))
            print(idinfo)

            user = self.mongo_db.db_find(
                "usuarios", False, {"email": idinfo["email"]})[0]

            if not user:
                sobrenome = idinfo["family_name"] or "nenhum"
                novo_usuario = {"email": idinfo["email"], "senha": "gerado_pelo_google",
                                "nome": idinfo["given_name"], "sobrenome": sobrenome}
                return self.registra(novo_usuario)

            access_token = self.encode_jwt(
                user["email"], user["tipoDeAcesso"])
            self.mongo_db.insert(
                "acessos", {"usuario": user["email"], "horario": datetime.utcnow()})

            return {"token": access_token}, 200
        except Exception as e:
            print(e)
            return {"errorMessage": "Token de senha inválido ou expirado"}, 401

    def altera_senha(self, jwt_para_reset, nova_senha):
        try:
            payload = jwt.decode(jwt_para_reset, os.getenv(
                "JWT_KEY"), algorithms=["HS256"])
            user = self.mongo_db.db_find(
                "usuarios", False, {"email": payload["reset_user"]})[0]
            user["senha"] = self.hash_senha(nova_senha)
            novo_user = self.mongo_db.patch("usuarios", user["_id"], user)
            if (novo_user[1] == 200):
                novo_user[0]['_id'] = str(novo_user[0]['_id'])
                return novo_user
            else:
                return {"errorMessage": "Ocorreu um erro ao atualizar a senha do usuário"}, 401
        except Exception as e:
            return {"errorMessage": "Token de senha inválido ou expirado"}, 401

    def envia_email_esqueci_senha(self, email):
        user = self.mongo_db.db_find(
            "usuarios", False, {"email": email})[0]
        if not user or "senha" not in user:
            return {"errorMessage": "Usuario nao encontrado."}, 401
        else:
            key = os.getenv("JWT_KEY")
            now = datetime.now(timezone.utc)
            expire = now + timedelta(hours=8)
            payload = dict(exp=expire, iat=now, sub="reset_user",
                           reset_user=user["email"])
            jwt_reset = jwt.encode(payload, key, algorithm="HS256")
            url = os.getenv("FRONT_URL") + "resetsenha?token=" + jwt_reset
            mensagem = get_message("Registre sua nova senha", email,
                                   f"<p>Por favor registre sua nova senha, acesse o <a href={url}> Link</a> para acessar a Games List, ou cole o link em seu navegador:</p><p>{url}</p>")
            if (send_mail(mensagem)):
                return {"message": "Email enviado"}, 200
            else:
                return {"errorMessage": "Problema ao enviar o email"}, 400

    def encode_jwt(self, usuario, tipo_de_acesso):
        now = datetime.now(timezone.utc)
        expire = now + timedelta(hours=8)
        payload = dict(exp=expire, iat=now, sub=usuario,
                       tipoDeAcesso=tipo_de_acesso)
        key = os.getenv("JWT_KEY")
        return jwt.encode(payload, key, algorithm="HS256")

    def registra(self, usuario):
        user_db = self.mongo_db.db_find(
            "usuarios", False, {"email": usuario["email"]})[0]
        if user_db:
            return {"errorMessage": "Usuario já cadastrado."}, 303

        usuario['tipoDeAcesso'] = "usuario"
        usuario['senha'] = self.hash_senha(usuario['senha'])
        self.mongo_db.insert("usuarios", usuario)

        access_token = self.encode_jwt(
            usuario["email"], usuario["tipoDeAcesso"])

        return {"token": access_token}, 200

    def hash_senha(self, senha_string):
        senha_string = senha_string.encode('utf-8')
        return bcrypt.hashpw(senha_string, bcrypt.gensalt()).decode('utf-8')

    def check_password(self, senha_string, senha_hash):
        senha_string = senha_string.encode('utf-8')
        senha_hash = senha_hash.encode('utf-8')
        return bcrypt.checkpw(senha_string, senha_hash)
