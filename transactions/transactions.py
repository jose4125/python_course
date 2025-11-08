import psycopg2 as bd

db_connection = bd.connect(
    user='curso_user',
    password='S3cret',
    host='localhost',
    port='5432',
    database='company'
)

print(db_connection)

try:
    cursor = db_connection.cursor()
    query = 'INSERT INTO employees (first_name, last_name, email) VALUES (%s, %s, %s);'
    values = ('maria', 'doe', 'mariadoe@gmail.com')
    cursor.execute(query, values)

    query2 = 'UPDATE employees SET first_name=%s, last_name=%s email=%s WHERE employee_id=%s;'
    values2 = ('juan', 'perez', 'juanperez@gmail.com', 102)
    cursor.execute(query2, values2)

    db_connection.commit()
    print('Transaction ended successfully')

except Exception as e:
    db_connection.rollback()
    print(f'Error, rollback applied: {e}')
finally:
    db_connection.close()
