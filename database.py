import psycopg2
from decouple import config


def data(champ):
    try:
        connection = psycopg2.connect(
            user='postgres',
            password='postgre',
            database='python2',
            host='localhost',
            port='5432'
        )
        query = '''
        create table if not exists winners(
        id SERIAL PRIMARY KEY,
        self_id int,
        total REAL check(total > 0),
        day_game DATE DEFAULT now()
        );
        '''
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        query_insert = '''
        insert into winners (self_id, total)
        values(%s, %s)
        '''
        # равно f'{наша переменная}{наша переменная}'
        cursor.execute(query_insert, (champ.id, champ.total))
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
            password='postgre',
            database='python2',
            host='localhost',
            port='5432'
        )
        cursor = connection.cursor()
        query = """
        select * from winners
        order by total DESC;
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





