from data_layer.connection import Connection
from logger import log

class PoolCursor:
    def __init__(self, connection = None, cursor = None):
        self.__connection = connection
        self.__cursor = cursor

    def __enter__(self):
        log.debug('Starting PoolCursor context manager with __enter__')
        self.__connection = Connection.get_connection()
        self.__cursor = self.__connection.cursor()

        return self.__cursor

    def __exit__(self, exception_type, exception_value, traceback):
        log.debug('Stopping PoolCursor context manager with __exit__')
        if exception_value:
            self.__connection.rollback()
            log.error(f'PoolCursor context manager rollback exception: {exception_value} - {exception_type} - {traceback}')

        else:
            self.__connection.commit()
            log.debug('PoolCursor context manager commit successful')

        self.__cursor.close()
        Connection.release_connection(self.__connection)


if __name__ == '__main__':
    with PoolCursor() as cursor:
        log.debug('Using PoolCursor in main block')
        cursor.execute('select * from employees')
        records = cursor.fetchall()
        log.debug(f'Records: {records}')