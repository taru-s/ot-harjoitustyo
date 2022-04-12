import os
import sqlite3


DIRNAME = os.path.dirname(__file__)

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.sqlite'

DATABASE_FILE = os.path.join(DIRNAME, "data", DATABASE_FILENAME)

CONNECTION = sqlite3.connect(DATABASE_FILE)
CONNECTION.row_factory = sqlite3.Row


def get_database_connection():
    return CONNECTION
