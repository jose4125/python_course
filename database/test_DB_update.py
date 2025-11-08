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
            query = 'UPDATE employees SET first_name=%s, last_name=%s, email=%s WHERE employee_id = %s ORDER BY employee_id;'
            values = ('juan', 'doe', 'juandoe@gmail.com', 103)
            cursor.execute(query, values)
            # with context manager handles commit automatically
            # db_connection.commit()
            employees_updated = cursor.rowcount
            print(f'Employees updated: {employees_updated}')
except Exception as e:
    print(f'Error: {e}')
finally:
    db_connection.close()
