from database import engine, SessionLocal
from models import Book, Student

# Criar a sessão do banco de dados
db = SessionLocal()

# Consultar todos os livros
books = db.query(Book).all()
print("Livros no banco de dados:")
for book in books:
    print(f"- {book.title}, Autor: {book.author}, Editora: {book.publisher}, Data: {book.published_date}")

# Consultar todos os estudantes
students = db.query(Student).all()
print("\nEstudantes no banco de dados:")
for student in students:
    print(f"- {student.name}")

# Fechar a sessão do banco de dados
db.close()


###Via GPT