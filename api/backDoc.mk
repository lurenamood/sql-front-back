EMPEZAR ENTRONO DE BACK con Python

1. Importar la libreria en main.py

Inicizialiar servidor web terminal CMD pongo , 
para poder hacer servir el CLI de FastAPI

!!![RECUERDA] 
	Tienes que estar dentro de enviroment en local!

	Instalar en CMD 
	- pip install "fastapi[standard]" --> si no te va

	- fastapi main.py

2. Instalar POSTMAN en version Desktop - Cuenta Github
	
	- pipenv install mysql-connector-python
	- pipenv install uvicorn


2.1 Crear un nuevo root ( user y password para la DATABASE)
	En mySQL

3. En mySQL crear DATABASE SIMPLE PARA COMPROBACIONES
	en consultas SQL, 
	hacer INSERT 
	que el Obj no quede vacio

4. ejecutar finalmente el backend para ver si funciona 
	- uvicorn main:app --reload


5. ESTRUCTURA DE CARPETAS version 1

| Ruta del archivo             | Función esperada                          |
|-----------------------------|-------------------------------------------|
| `api/app/main.py`           | Punto de entrada del servidor FastAPI     |
| `api/app/core/config.py`    | Variables de entorno y configuración      |
| `api/app/core/database.py`  | Conexión a la base de datos (SQLAlchemy)  |
| `api/app/models/user.py`    | Modelo de usuario con SQLAlchemy          |
| `api/app/schemas/user.py`   | Validaciones Pydantic                     |
| `api/app/crud/user.py`      | Lógica CRUD (create/read/update/delete)   |
| `api/app/routes/user.py`    | Endpoints FastAPI                         |
| `api/app/auth/firebase.py`  | Verificación de Firebase JWT              |
| `api/app/utils/security.py` | Funciones auxiliares (hash, seguridad)    |

ESTRUCTURA version 2

backend/
├── main.py                  # Arranca FastAPI
├── core/                   # Configuraciones generales
│   ├── config.py
│   └── firebase.py         # Inicializa Firebase Admin SDK
├── auth/
│   ├── dependencies.py     # verify_token() y auth helpers
│   └── routes.py           # /login /protected /me etc
├── models/
│   └── user.py             # Usuario SQLAlchemy model
├── schemas/
│   └── user.py             # Pydantic User schemas
├── routes/
│   └── protected.py        # Rutas que requieren login
├── utils/
│   └── db.py               # Conexión MySQL


	
CONCEPTOS - REGLAS

En python no crear nombre-apellido.py 
		Así si     nombre_apellido.py

uvicorn ---> POSTMAN
	es para ejecutar FastAPI en un Server en Python


---------------------------------------------------------
RESUMEN DE COMANDOS 
python -m venv env
pip install fastapi uvicorn mysql-connector-python
pip install "fastapi[standard]"
uvicorn main:app --reload --> ACTIVAR Terminal PROYECTO

----------------------------------------------------------------


CONECTAR CON EL FRONT-Nextjs


