    """Establishes the sqlite3 database connection.

    Gets the file name from environment or restorts to the default file name.

    Provides the funcion get_database_connection(), which returns the database connection.
    """

import os
import sqlite3


DIRNAME = os.path.dirname(__file__)

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.sqlite'

DATABASE_FILE = os.path.join(DIRNAME, "data", DATABASE_FILENAME)

CONNECTION = sqlite3.connect(DATABASE_FILE)
CONNECTION.row_factory = sqlite3.Row


def get_database_connection():
    return CONNECTION
