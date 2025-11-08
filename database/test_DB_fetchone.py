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
            query = 'SELECT employee_id, first_name  FROM employees WHERE employee_id = %s;'
            employee_id = input('Enter employee ID: ')
            cursor.execute(query, (employee_id,))
            employee = cursor.fetchone()
            print(employee)
except Exception as e:
    print(f'Error: {e}')
finally:
    db_connection.close()