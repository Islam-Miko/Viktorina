import psycopg2
from psycopg2.extras import RealDictCursor, NamedTupleCursor
from decouple import config

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
    SELECT op.*, cu.first_name FROM operations op
    JOIN customers cu ON op.owner_id=cu.id;
    """

    query2 = """
    CREATE TABLE python2 (
    id SERIAL,
    name VARCHAR(5)
    );
    """
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        print(i.id, i.price)
    connection.commit()
except Exception as e:
    print(e)
finally:
    if connection:
        cursor.close()
        connection.close()
