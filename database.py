import psycopg2
from psycopg2.extras import NamedTupleCursor
from decouple import config


def decor_connection(func):
    def wrapper(*args, **kwargs):
        try:
            connection = psycopg2.connect(
                user=config('DB_USER'),
                password=config('DB_PSD'),
                database=config('DB'),
                host='localhost',
                port='5432',
                cursor_factory=NamedTupleCursor
                )

            cursor = connection.cursor()
            result = func(cursor=cursor, connection=connection, *args, **kwargs)
            connection.commit()
            return result
        except Exception as e:
            print(e)
        finally:
            if connection:
                cursor.close()
                connection.close()

    return wrapper


@decor_connection
def create_table(**kwargs):
    cursor = kwargs.get('cursor')
    query = """
    CREATE TABLE IF NOT EXISTS winners(
    id SERIAL PRIMARY KEY,
    login VARCHAR(50),
    name VARCHAR(50),
    score REAL CHECK (score > 0),
    day_of_game DATE DEFAULT now()
    );
    """
    cursor.execute(query)


@decor_connection
def create_table_registered(**kwargs):
    cursor = kwargs.get('cursor')
    query = """
    CREATE TABLE IF NOT EXISTS players(
    id SERIAL PRIMARY KEY,
    username varchar(30),
    password varchar(30)
    );
    """
    cursor.execute(query)


@decor_connection
def insert_in_table(login, username, score, spend_time, **kwargs):
    cursor = kwargs.get('cursor')
    query = """
    INSERT INTO winners (login, name, score, day_of_game) 
    VALUES(%s, %s, %s, %s);
    """
    cursor.execute(query, (login, username, score, spend_time))


@decor_connection
def get_from_db(login, **kwargs):
    cursor = kwargs.get('cursor')
    query = """
    SELECT * FROM winners
    WHERE login LIKE %s
    ORDER BY score DESC;
    """
    cursor.execute(query, (login,))
    result = cursor.fetchall()
    for tb in result:
        print(tb)


@decor_connection
def registration(username, password, **kwargs):
    cursor = kwargs.get('cursor')
    query = """
    INSERT INTO players (username, password) 
    VALUES(%s, %s);
    """
    cursor.execute(query, (username, password))


@decor_connection
def get_users_from_table(**kwargs):
    cursor = kwargs.get('cursor')
    query = """
    SELECT * FROM players;"""
    cursor.execute(query)
    result = cursor.fetchall()
    return result

