from database import engine, SessionLocal
from models import Book
from datetime import date

# Criar a sessão do banco de dados
db = SessionLocal()

# Criar um objeto Book para adicionar ao banco
book = Book(
    title="1984",
    author="George Orwell",
    publisher="Harper",
    published_date=date(1949, 6, 8),
    cover_image="https://link_imagem.com"
)

# Adicionar e confirmar a transação no banco de dados
db.add(book)
db.commit()

print(f"{book.title} adicionado ao banco de dados com sucesso!")

# Fechar a sessão do banco de dados
db.close()

from database import engine, SessionLocal
from models import Student

# Criar a sessão do banco de dados
db = SessionLocal()

# Criar um objeto Student para adicionar ao banco
student = Student(name="João Silva")

# Adicionar e confirmar a transação no banco de dados
db.add(student)
db.commit()

print(f"{student.name} adicionado ao banco de dados com sucesso!")

# Fechar a sessão do banco de dados
db.close()

###Via GPT