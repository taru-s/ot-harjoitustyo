import os
import sqlite3


dirname = os.path.dirname(__file__)

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.sqlite'

database_file = os.path.join(dirname, "data", DATABASE_FILENAME)

connection = sqlite3.connect(database_file)
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection
