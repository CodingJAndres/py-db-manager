from sqlalchemy.orm import Session
from database import User, Post

# Crear un nuevo usuario
def create_user(db: Session, name: str, email: str):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Obtener todos los usuarios
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# Crear un nuevo post
def create_post(db: Session, title: str, content: str, author_id: int):
    db_post = Post(title=title, content=content, author_id=author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
