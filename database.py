import psycopg2
from psycopg2.extras import NamedTupleCursor
from decouple import config


def create_table():
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

        query = """
        CREATE TABLE IF NOT EXISTS winners(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        score REAL CHECK (score > 0),
        day_of_game DATE DEFAULT now()
        );
        """
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        if connection:
            cursor.close()
            connection.close()


def insert_in_table(username, score, spend_time):
    try:
        connection = psycopg2.connect(
            user=config('DB_USER'),
            password=config('DB_PSD'),
            database=config('DB'),
            host='localhost',
            port='5432',
            cursor_factory=NamedTupleCursor)
        cursor = connection.cursor()
        query = """
        INSERT INTO winners (name, score, day_of_game) 
        VALUES(%s, %s, %s);
        """
        cursor.execute(query, (username, score, spend_time))
        connection.commit()
    except Exception as e:
        print(e)

    finally:
        if connection:
            cursor.close()
            connection.close()


def get_from_db():
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
        query = """
        SELECT * FROM winners;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        for tb in result:
            print(tb)
    except Exception:
        print(Exception)
    finally:
        if connection:
            cursor.close()
            connection.close()
