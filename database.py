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
            func(cursor=cursor, *args, **kwargs)
            connection.commit()
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
    name VARCHAR(50),
    score REAL CHECK (score > 0),
    day_of_game DATE DEFAULT now()
    );
    """
    cursor.execute(query)


@decor_connection
def insert_in_table(username, score, spend_time, **kwargs):
    cursor = kwargs.get('cursor')
    query = """
    INSERT INTO winners (name, score, day_of_game) 
    VALUES(%s, %s, %s);
    """
    cursor.execute(query, (username, score, spend_time))


@decor_connection
def get_from_db(**kwargs):
    cursor = kwargs.get('cursor')
    query = """
    SELECT * FROM winners
    ORDER BY score DESC;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    for tb in result:
        print(tb)

