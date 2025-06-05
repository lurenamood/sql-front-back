# api/app/core/database.py

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="primeraapi-for-react"
    )

def get_cursor():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    return conn, cursor
