import psycopg2
from decouple import config


def data(winner):
    try:
        connection = psycopg2.connect(
            user=config('DB_USER'),
            password=config('DB_PSD'),
            database=config('DB'),
            host='localhost',
            port='5432',
        )

        cursor = connection.cursor()

        query = """
        CREATE TABLE IF NOT EXISTS winners(
        id SERIAL PRIMARY KEY,
        name VARCHAR(15),
        self_id int,
        total REAL check(total > 0),
        day_game DATE DEFAULT now()
        );
        """
        cursor.execute(query)
        connection.commit()

        query_insert = """
        INSERT INTO winners (self_id, total)
        VALUES(%s, %s)
        """
        cursor.execute(query_insert, (winner.id, winner.total))
        connection.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


def read_db():
    try:
        connection = psycopg2.connect(
            user=config('DB_USER'),
            password=config('DB_PSD'),
            database=config('DB'),
            host='localhost',
            port='5432',
        )
        cursor = connection.cursor()
        query = """
        SELECT * FROM winners
        ORDER BY total DESC;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as exp:
        print(exp)
    finally:
        connection.close()
        cursor.close()
