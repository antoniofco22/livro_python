from pydantic import BaseModel
from datetime import date

class LivroSchema(BaseModel):
    titulo: str
    autor: str
    data_publicacao: date
    editora: str
    url_capa: str

class EstudanteSchema(BaseModel):
    nome: str

class EmprestimoSchema(BaseModel):
    id_livro: int
    id_estudante: int
    data_emprestimo: date
