from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_BANCO_DE_DADOS = "sqlite:///./test.db"

#donectar
engine = create_engine(URL_BANCO_DE_DADOS)
SessaoLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()