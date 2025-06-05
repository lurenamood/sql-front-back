# api/app/crud/user.py
from fastapi import HTTPException
from app.schemas.user_schema import UserUpdate
from ..core.database import get_db_connection


# from fastapi import HTTPException
# from api.database import get_db_connection

def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT US_id, US_name FROM usuarios")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def create_user(user: dict):
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = "INSERT INTO usuarios (US_name, US_surname, US_email) VALUES (%s, %s, %s)"
    cursor.execute(
        insert_query, (user["US_name"], user["US_surname"], user["US_email"]))
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "User created successfully"}


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


def set_user_inactive(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Verificar si el usuario existe
    cursor.execute("SELECT * FROM usuarios WHERE US_id = %s", (user_id,))
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Cambiar el estado a INACTIVO
    cursor.execute(
        "UPDATE usuarios SET estado = 'inactivo' WHERE US_id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Usuario dado de baja (inactivo)"}
