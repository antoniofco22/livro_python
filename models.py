from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    autor = Column(String)
    editora = Column(String)
    data_publicacao = Column(Date)
    imagem_capa = Column(String)

class Estudante(Base):
    __tablename__ = "estudantes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)

class Emprestimo(Base):
    __tablename__ = "emprestimos"
    id = Column(Integer, primary_key=True, index=True)
    id_livro = Column(Integer, ForeignKey("livros.id"))
    id_estudante = Column(Integer, ForeignKey("estudantes.id"))
    data_emprestimo = Column(Date)

    livro = relationship("Livro")
    estudante = relationship("Estudante")