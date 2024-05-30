import sqlite3
import os

# Ruta completa a la base de datos
database_path = '/home/scobosga/ethbots/database/ethbot.db'

def check_database_file():
    """
    Verifica que el archivo de la base de datos existe y tiene los permisos adecuados.
    """
    if not os.path.exists(database_path):
        raise FileNotFoundError(f"El archivo de la base de datos no existe: {database_path}")
    if not os.access(database_path, os.R_OK):
        raise PermissionError(f"El archivo de la base de datos no tiene permisos de lectura: {database_path}")
    if not os.access(database_path, os.W_OK):
        raise PermissionError(f"El archivo de la base de datos no tiene permisos de escritura: {database_path}")

def drop_table(table_name):
    """
    Elimina una tabla específica en la base de datos.
    """
    check_database_file()
    
    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        conn.commit()
        print(f"Tabla {table_name} eliminada.")

if __name__ == "__main__":
    # Nombre de la tabla a eliminar
    table_name = "CobosDS_botests"  # Reemplaza con el nombre de la tabla que deseas eliminar
    
    try:
        drop_table(table_name)
        print(f"Tabla {table_name} ha sido eliminada.")
    except Exception as e:
        print(f"Error: {e}")
