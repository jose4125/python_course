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
            query = 'SELECT * FROM employees;'
            cursor.execute(query)
            employees = cursor.fetchall()
            print(employees)
except Exception as e:
    print(f'Error: {e}')
finally:
    db_connection.close()
