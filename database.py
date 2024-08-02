from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from config import DATABASE_URL

# Crear el motor de base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear una base declarativa
Base = declarative_base()

# Definir los modelos
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")

# Inicializar la base de datos
def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        print("Base de datos inicializada correctamente.")
    except SQLAlchemyError as e:
        print(f"Error al inicializar la base de datos: {e}")

# Configurar la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
