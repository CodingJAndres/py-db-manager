from sqlalchemy.orm import Session
from database import init_db, get_db
from crud import create_user, get_users, create_post

def main():
    # Inicializar la base de datos
    init_db()
    
    # Obtener una sesión de base de datos
    db = next(get_db())
    
    # Crear usuarios
    user1 = create_user(db, name="Alice", email="alice@example.com")
    user2 = create_user(db, name="Bob", email="bob@example.com")
    print(f"Usuarios creados: {user1}, {user2}")
    
    # Obtener todos los usuarios
    users = get_users(db)
    print(f"Usuarios en la base de datos: {users}")
    
    # Crear un post para el primer usuario
    post1 = create_post(db, title="First Post", content="This is the content of the first post.", author_id=user1.id)
    print(f"Post creado: {post1}")

if __name__ == "__main__":
    main()
