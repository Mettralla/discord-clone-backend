from decouple import config
import mysql.connector

class DatabaseConnection:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host="127.0.0.1",
                user= config("MYSQL_USER"),
                port= "3306",
                password= config("MYSQL_PASSWORD"),
                database= "discord_clone_db"
            )
        return cls._connection

    @classmethod
    def execute_query(cls, query, params=None):
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        cursor.close()

    @classmethod
    def fetch_one(cls, query, params=None):
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result

    @classmethod
    def fetch_all(cls, query, params=None):
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        cursor.close()
        return results

    @classmethod
    def close_connections(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connections = None
