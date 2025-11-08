from data_layer.person import Person
from data_layer.logger import log
from data_layer.pool_cursor import PoolCursor


class PersonDAO:
    """
    DAO (Data Access Object) for the Person class to handle database operations.
    """
    __select: str = 'SELECT * FROM persons ORDER BY person_id'
    __insert: str = 'INSERT INTO persons(name, last_name, email) VALUES (%s, %s, %s)'
    __update: str = 'UPDATE persons SET name = %s, last_name = %s, email = %s WHERE person_id = %s'
    __delete: str = 'DELETE FROM persons WHERE person_id = %s'

    @classmethod
    def select(cls):
        with PoolCursor() as cursor:
            cursor.execute(cls.__select)
            records = cursor.fetchall()
            persons_list = []

            for record in records:
                new_person = Person(record[0], record[1], record[2], record[3])
                persons_list.append(new_person)

            return persons

    @classmethod
    def insert(cls, new_person: Person):
        with PoolCursor() as cursor:
            values = (new_person.name, new_person.last_name, new_person.email)
            cursor.execute(cls.__insert, values)
            log.debug(f'Inserting new person: {new_person}')

            return cursor.rowcount

    @classmethod
    def update(cls, new_person: Person):
        with PoolCursor() as cursor:
            values = (new_person.name, new_person.last_name, new_person.email, new_person.person_id)
            cursor.execute(cls.__update, values)
            log.debug(f'Updating person: {new_person}')

            return cursor.rowcount

    @classmethod
    def delete(cls, delete_person: Person):
        with PoolCursor() as cursor:
            values = (delete_person.person_id,)
            cursor.execute(cls.__delete, values)
            log.debug(f'Deleting person: {delete_person}')

            return cursor.rowcount


if __name__ == '__main__':
    person1 = Person(1, 'Juan', 'Perez', 'juanperez@gmail.com')
    total_updated_person = PersonDAO.update(person1)
    log.debug(f'Updated person: {total_updated_person}')

    person2 = Person(name = 'Carlos', last_name = 'Santana', email = 'carlossantana@gmail.com')
    total_inserted_person = PersonDAO.insert(person2)
    log.debug(f'Inserted person: {total_inserted_person}')

    person3 = Person(person_id = 4)
    total_deleted_person = PersonDAO.delete(person3)
    log.debug(f'Deleted person: {total_deleted_person}')

    persons = PersonDAO.select()
    for person in persons:
        log.debug(person)