import psycopg2

db_connection = psycopg2.connect(
    user='curso_user',
    password='S3cret',
    host='localhost',
    port='5432',
    database='company'
)

print(db_connection)

try:
    with db_connection:
        with db_connection.cursor() as cursor:
            query = 'INSERT INTO employees(first_name, last_name, email) VALUES(%s, %s, %s);'
            values = ('john', 'doe', 'jhondoe@gmail.com')
            cursor.execute(query, values)
            # with context manager handles commit automatically
            # db_connection.commit()
            employees_inserted = cursor.rowcount
            print(f'Employees inserted: {employees_inserted}')
except Exception as e:
    print(f'Error: {e}')
finally:
    db_connection.close()
