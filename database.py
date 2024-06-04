import os
import sqlite3

# Define the path to the SQLite database file.
database_path = os.path.join(os.path.dirname(__file__), 'database', 'ethicalbot.db')

def get_db_connection():
    """
    Establishes a connection to the SQLite database.

    This function connects to the SQLite database specified by the database_path.
    It also sets the row_factory attribute to sqlite3.Row to allow dictionary-like
    access to rows, making it easier to work with query results.

    :return: A connection object to the SQLite database.
    """
    conn = sqlite3.connect(database_path)
    conn.row_factory = sqlite3.Row
    return conn
