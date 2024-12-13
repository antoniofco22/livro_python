from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from datetime import date
from auth import criar_token_acesso, autenticar_usuario, verificar_token
from database import engine, Base, SessaoLocal
from models import Livro, Estudante, Emprestimo
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#sessão do banco de dados
def obter_sessao_db():
    db = SessaoLocal()
    try:
        yield db
    finally:
        db.close()

# modelo login
class DadosLogin(BaseModel):
    usuario: str
    senha: str

#rota login admin
@app.post("/login/")
async def login(dados: DadosLogin):
    if autenticar_usuario(dados.usuario, dados.senha):
        token = criar_token_acesso({"sub": dados.usuario})
        return {"token_de_acesso": token}
    raise HTTPException(status_code=403, detail="usuario ou senha errado")

#autenticacao
async def obter_usuario_atual(token: str = Depends(oauth2_scheme)):
    credenciais = verificar_token(token)
    if not credenciais:
        raise HTTPException(status_code=403, detail="token invalido")
    return credenciais

#emprestar
@app.post("/emprestar/")
async def emprestar_livro(id_livro: int, id_estudante: int, db: Session = Depends(obter_sessao_db)):
    emprestimo = Emprestimo(book_id=id_livro, student_id=id_estudante, borrow_date=date.today())
    db.add(emprestimo)
    db.commit()
    return {"mensagem": "emprestimo feito!"}
