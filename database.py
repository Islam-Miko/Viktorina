import psycopg2
from decouple import config


def data(champ):
    try:
        print(type(champ), champ)
        connection = psycopg2.connect(
            user = 'postgres',
            password = 'python2021',
            database = 'python',
            host = 'localhost',
            port = '5432'
        )
        query = """
        CREATE TABLE IF NOT EXISTS winners(
        id SERIAL PRIMARY KEY,
        self_id int,
        total REAL check(total > 0),
        day_game DATE DEFAULT now()
        );
        """
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        query_insert = """
        INSERT INTO winners (self_id, total)
        VALUES(%s, %s)
        """
        # равно f"{наша переменная}{наша переменная}"
        cursor.execute(query_insert,(champ.id, champ.total))
        connection.commit()
    except Exception as exp:
        print(exp)
    finally:
        connection.close()
        cursor.close()


def read_db():
    try:
        connection = psycopg2.connect(
            user='postgres',
            password='python2021',
            database='python',
            host='localhost',
            port='5432'
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


