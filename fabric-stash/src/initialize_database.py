from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS Fabrics;
    ''')

    connection.commit()


def create_tables(connection):
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
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)
