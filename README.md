# py-db-manager

**py-db-manager** es un proyecto en Python diseñado para facilitar la gestión de bases de datos utilizando **SQLAlchemy** y **PostgreSQL**. Este proyecto incluye scripts para configurar una base de datos, realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y demostrar el uso básico de estas funcionalidades.

## Requisitos

- Python 3.8 o superior
- [SQLAlchemy](https://www.sqlalchemy.org/) (para la gestión de la base de datos)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) (conector para PostgreSQL)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (para gestionar variables de entorno)

## Instalación

1. **Clona o descarga el repositorio:**

    ```bash
    git clone https://github.com/tu_usuario/py-db-manager.git
    ```

2. **Navega al directorio del proyecto:**

    ```bash
    cd py-db-manager
    ```

3. **Crea un archivo `.env` en el directorio raíz del proyecto y define la URL de tu base de datos:**

    ```
    DATABASE_URL=postgresql://user:password@localhost/mydatabase
    ```

4. **Instala las dependencias necesarias:**

    ```bash
    pip install -r requirements.txt
    ```

    Asegúrate de que el archivo `requirements.txt` contenga las siguientes líneas:

    ```
    sqlalchemy
    psycopg2-binary
    python-dotenv
    ```

## Scripts

### Inicialización de la Base de Datos

Este script configura la base de datos y crea las tablas necesarias.

#### Uso

1. **Ejecuta el script de inicialización:**

    ```bash
    python database.py
    ```

2. **El script creará las tablas en la base de datos según el modelo definido.**

### Operaciones CRUD

El script principal proporciona ejemplos de cómo utilizar las funciones CRUD para interactuar con la base de datos.

#### Uso

1. **Ejecuta el script principal:**

    ```bash
    python main.py
    ```

2. **El script demostrará la creación de usuarios y posts y mostrará los resultados en la consola.**

#### Descripción de Funciones

- **`create_user(name, email)`**: Crea un nuevo usuario con el nombre y correo electrónico proporcionados.
- **`get_users(skip, limit)`**: Obtiene una lista de usuarios, con opciones para paginación.
- **`create_post(title, content, author_id)`**: Crea un nuevo post asociado al usuario con el ID proporcionado.

### Manejo de Errores

- **Errores de Conexión:** Se muestran mensajes de error si no se puede conectar a la base de datos o si ocurren problemas al ejecutar las consultas.
- **Errores de Inicialización:** El script `database.py` maneja errores durante la creación de tablas y proporciona mensajes claros.

## Documentación

- **`config.py`**: Configura las variables de entorno necesarias para conectar con la base de datos.
- **`database.py`**: Define el esquema de la base de datos y maneja la inicialización.
- **`crud.py`**: Contiene funciones para operaciones CRUD.
- **`main.py`**: Muestra ejemplos de uso de las funciones CRUD.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---

Utiliza **py-db-manager** para configurar y gestionar una base de datos relacional en Python de manera efectiva y flexible.
