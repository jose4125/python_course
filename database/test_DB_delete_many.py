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
            query = 'DELETE FROM employees WHERE employee_id IN %s;'
            input_values = input('Enter employee IDs to delete (separated by comma): ')
            values = (tuple(input_values.split(',')),)
            cursor.execute(query, values)
            # with context manager handles commit automatically
            # db_connection.commit()
            employees_deleted = cursor.rowcount
            print(f'Employees updated: {employees_deleted}')
except Exception as e:
    print(f'Error: {e}')
finally:
    db_connection.close()
