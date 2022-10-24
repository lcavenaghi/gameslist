from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from flask import jsonify
from common.mongo_db import MongoDb
import os
import jwt
import bcrypt

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

        self.mongo_db.insert("acessos", {"usuario":user["email", "horario": datetime.utcnow()]})

        return {"token": access_token}, 200

    def encode_jwt(self, usuario, tipo_de_acesso):
        now = datetime.now(timezone.utc)
        expire = now + timedelta(hours=8)
        payload = dict(exp=expire, iat=now, sub=usuario,
                       tipoDeAcesso=tipo_de_acesso)
        key = os.getenv("JWT_KEY")
        return jwt.encode(payload, key, algorithm="HS256")
    
    def registra(self, usuario):
        user = self.mongo_db.db_find("usuarios", False, {"email": usuario["email"]})[0]
        if user:
            return {"errorMessage": "Usuario já cadastrado."}, 401
            
        usuario['senha'] = self.hash_senha(usuario['senha'])
        self.mongo_db.insert("usuarios", usuario)

        access_token = self.encode_jwt(
            user["email"], user["tipoDeAcesso"])

        return {"token": access_token}, 200

    def hash_senha(self, senha_string):
        senha_string = senha_string.encode('utf-8')
        return bcrypt.hashpw(senha_string, bcrypt.gensalt())

    def check_password(self, senha_string, senha_hash):
        senha_string = senha_string.encode('utf-8')
        senha_hash = senha_hash.encode('utf-8')
        return bcrypt.checkpw(senha_string, senha_hash)
