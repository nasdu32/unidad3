# datos/conexion_db.py
import sqlite3

def obtener_conexion():
    return sqlite3.connect("base_datos.db")
