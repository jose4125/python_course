from __future__ import annotations
from logger import log
from psycopg2 import pool
import sys

class Connection:
    __database: str = 'company'
    __user: str = 'curso_user'
    __password: str = 'S3cret'
    __port: str = '5432'
    __host: str = 'localhost'
    __min_connections: int = 1
    __max_connections: int = 5
    __pool = None

    @classmethod
    def get_pool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(
                    cls.__min_connections,
                    cls.__max_connections,
                    user = cls.__user,
                    password = cls.__password,
                    host = cls.__host,
                    port = cls.__port,
                    database = cls.__database
                )

                log.debug(f'Connection pool created successfully: {cls.__pool}')
                return cls.__pool
            except Exception as e:
                log.error(f'Error creating connection pool: {e}')
                sys.exit()

        return cls.__pool

    @classmethod
    def get_connection(cls):
        connection = cls.get_pool().getconn()
        log.debug(f'Connection pool created successfully: {connection}')
        return connection

    @classmethod
    def release_connection(cls, connection: Connection):
        cls.get_pool().putconn(connection)
        log.debug(f'Connection returned to pool: {connection}')

    @classmethod
    def close_connection(cls):
        cls.get_pool().closeall()
        log.debug(f'Connection closed successfully: {cls.get_pool()}')


if __name__ == '__main__':
    connection1 = Connection.get_connection()
    connection1.release_connection()
    connection2 = Connection.get_connection()