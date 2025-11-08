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
            query = 'SELECT employee_id, first_name  FROM employees WHERE employee_id IN %s;'
             # employee_ids = ((100, 102, 104),)
            employee_id_values = input('Enter employee IDs (separated by comma): ')
            employee_ids = (tuple(employee_id_values.split(',')),)
            cursor.execute(query, employee_ids)
            employees = cursor.fetchall()

            for employee in employees:
                print(employee)
except Exception as e:
    print(f'Error: {e}')
finally:
    db_connection.close()
