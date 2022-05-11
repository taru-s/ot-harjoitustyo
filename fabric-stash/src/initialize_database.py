from database_connection import get_database_connection


def drop_tables(connection):
    """Drops the sqlite database table Fabrics, if it exists.

    Args:
        connection (): sqlite3 database connection
    """
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS Fabrics;
    ''')

    connection.commit()


def create_tables(connection):
    """Creates sqlite database table Fabrics.

    Args:
        connection (): sqlite3 database connection
    """
    cursor = connection.cursor()

    cursor.execute('''
        create table Fabrics (
            id INTEGER PRIMARY KEY,
            name TEXT,
            width INTEGER,
            length INTEGER,
            washed INTEGER
        );
    ''')

    connection.commit()


def initialize_database():
    """Initializes sqlite database.

    Gets the database connection from the database_connection.py file.
    Drops exsisting tables and creates new tables.
    """
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
