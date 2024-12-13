from jose import JWTError, jwt
from datetime import datetime, timedelta

#chave secreta
CHAVE_SECRETA = "antonio_francisco"
ALGORITMO = "HS256"

#admin
CREDENCIAIS_ADMIN = {
    "usuario": "admin",
    "senha": "admin"
}

def criar_token_acesso(dados: dict):
    to_encode = dados.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=30)})
    return jwt.encode(to_encode, CHAVE_SECRETA, algorithm=ALGORITMO)

def verificar_token(token):
    try:
        payload = jwt.decode(token, CHAVE_SECRETA, algorithms=[ALGORITMO])
        return payload
    except JWTError:
        return None

def autenticar_usuario(usuario: str, senha: str):
    return usuario == CREDENCIAIS_ADMIN["usuario"] and senha == CREDENCIAIS_ADMIN["senha"]