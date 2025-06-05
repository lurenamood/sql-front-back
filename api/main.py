'''from fastapi import FastAPI, Body, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import os
from pydantic import BaseModel  # usuarios gmail
from routing import APIRouter


app = FastAPI()

# Permitir peticiones desde el frontend (Next.js en localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Control de errores


@app.on_event("startup")
def startup_db_check():
    try:
        conn = get_db_connection()
        print("✅ Conexión a MySQL exitosa.")
        conn.close()
    except Exception as e:
        print("❌ Error al conectar a MySQL:", e)

# Configuración de conexión a MySQL


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="primeraapi-for-react"
    )


@app.get("/usuarios")
def get_users():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT US_id, US_name FROM usuarios")
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results
    except Exception as e:
        return {"error": str(e)}

# insertar usuario


@app.post("/users/create", status_code=status.HTTP_201_CREATED)
def create_user(user: dict = Body()):
    connection = get_db_connection()
    cursor = connection.cursor()

    insert_query = "INSERT INTO usuarios (US_name, US_surname, US_email) VALUES (%s, %s, %s)"
    cursor.execute(
        insert_query, (user["US_name"], user["US_surname"], user["US_email"]))
    connection.commit()

    cursor.close()
    connection.close()
    return {"message": "User created successfully"}



# @app.patch("/users/{user_id}", status_code=status.HTTP_200_OK)
# def update_user(user_id: int, updated_fields: dict = Body(...)):
#     connection = get_db_connection()
#     cursor = connection.cursor()

#     # Construir dinámicamente el SET del UPDATE
#     set_clause = ", ".join([f"{key} = %s" for key in updated_fields.keys()])
#     values = list(updated_fields.values())

#     update_query = f"UPDATE usuarios SET {set_clause} WHERE US_id = %s"
#     cursor.execute(update_query, values + [user_id])
#     connection.commit()

#     cursor.close()
#     connection.close()

#     return {"message": "User updated successfully"} 




# @app.get("/users{user_id}")


# @app.get("/selectbyparams/users")
# def select_by_parameters(id: int):
#     select_query = "SELECT * FROM usuarios WHERE US_id = %s"
#     cursor.execute(select_query, (id,))
#     result = cursor.execute.fetchone()
#     if not result:
#         raise HTTPException(status_code=status.HTTTP_404_NOT_FOUND, detail="User not found")
#     return result


class Usuario(BaseModel):
    id: int
    US_email: str
    US_name: str
    US_surname: str


#  obtener usuarios con cualquier email según la petición
@app.get("/filteremail/users")
def get_users_by_email_domain(domain: str):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    like_pattern = f"%@{domain}"
    query = "SELECT US_id, US_email, US_name, US_surname FROM usuarios WHERE US_email LIKE %s"
    cursor.execute(query, (like_pattern,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results



# actualiza los datos
class UserUpdate(BaseModel):
    US_id: int
    US_name: str
    US_surname: str
    US_email: str


@app.put("/users/update_state", status_code=status.HTTP_200_OK)
def update_user_fields(user: UserUpdate):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios WHERE US_id = %s", (user.US_id,))
    current = cursor.fetchone()

    if not current:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    

    save_user_to_history(cursor, current)

    cursor.execute("""
        UPDATE usuarios
        SET US_name = %s, US_surname = %s, US_email = %s
        WHERE US_id = %s
    """, (user.US_name, user.US_surname, user.US_email, user.US_id))

    connection.commit()
    cursor.close()
    connection.close()

    return {"message": "Usuario actualizado"}


# guarda historial, por si acaso del usuario que cambia los datos
def save_user_to_history(cursor, user_data): 
    insert = """
        INSERT INTO historial_cambios_datos (UP_id, UP_name, UP_surname, UP_email)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert, (
        user_data["UP_id"],
        user_data["UP_name"],
        user_data["UP_surname"],
        user_data["UP_email"]
    ))
'''

'''Mirar como hacerlo de otra manera el LOGIN y el DELETE'''
# @app.put("/update_state", status_code=status.HTTP_200_OK) # es como un POST
# def update_user_fields():
#     get_db_connection()
#     cursor = connection.cursor()

#     insert_query = "UPDATE INTO usuarios (US_name, US_surname, US_email) VALUES (%s, %s, %s)"
#     cursor.execute(
#     insert_query, (user["US_name"], user["US_surname"], user["US_email"]))
#     connection.commit()

# # 
#     if not result:
#         raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail="Error: User not modified")

'''ESTADO ACTIVO/INACTIVO del usuaria/o'''
# @app.delete()


'''primer GET ramón'''
# @app.get("/items")
# def get_items():

#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)

#     # Cambia `items` por tu tabla real
#     cursor.execute("SELECT id, name FROM usuarios")
#     results = cursor.fetchall()

#     cursor.close()
#     connection.close()

#     return results

# from fastapi import FastAPI
# from connect_mysql import get_cursor

# app = FastAPI()


# mydb, cursor = get_cursor() # instaciamos el cursor

''' Comprobaciones por Saludos de APIS'''
# @app.get("/users")
# def select_users():
#     select_query = "SELECT * FROM usuarios"
#     cursor.execute(select_query)
#     results = cursor.fetchall()
#     return results

# @app.get("/api/ruta1") # el BACK tiene que dar esta información para el Endpoint
# async def saludo():
#     return{"message":"Hiiiii, all OK"}

# @app.get("/api/ruta2")
# async def saludo():
#     return{"message":"Comprobando ruta2"}
