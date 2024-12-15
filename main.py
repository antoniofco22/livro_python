from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from datetime import date
from auth import criar_token_acesso, autenticar_usuario, verificar_token
from database import engine, Base, SessaoLocal
from models import Livro, Estudante, Emprestimo
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Adicionando o middleware de CORS
origins = [
    "http://localhost:3000",  # Exemplo para ambiente local
    "https://antoniofco22.github.io",  # Substitua pelo domínio do seu front-end
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir essas origens
    allow_credentials=True,  # Permitir cookies e autenticação
    allow_methods=["*"],  # Permitir todos os métodos
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Sessão do banco de dados
def obter_sessao_db():
    db = SessaoLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo de login
class DadosLogin(BaseModel):
    usuario: str
    senha: str

# Rota de login para admin
@app.post("/login/")
async def login(dados: DadosLogin):
    if autenticar_usuario(dados.usuario, dados.senha):
        token = criar_token_acesso({"sub": dados.usuario})
        return {"token_de_acesso": token}
    raise HTTPException(status_code=403, detail="Usuário ou senha errados")

# Autenticação
async def obter_usuario_atual(token: str = Depends(oauth2_scheme)):
    credenciais = verificar_token(token)
    if not credenciais:
        raise HTTPException(status_code=403, detail="Token inválido")
    return credenciais

# Empréstimo de livro
@app.post("/emprestar/")
async def emprestar_livro(id_livro: int, id_estudante: int, db: Session = Depends(obter_sessao_db)):
    emprestimo = Emprestimo(book_id=id_livro, student_id=id_estudante, borrow_date=date.today())
    db.add(emprestimo)
    db.commit()
    return {"mensagem": "Empréstimo feito com sucesso!"}
