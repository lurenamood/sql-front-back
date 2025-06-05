import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root", # crear un root en mysql
        password="", # crear un root en mysql
        database="primeraapi-for-react"   # poner tu DataBase creada
    )


def get_cursor(): # mirar concepto
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    return conn, cursor