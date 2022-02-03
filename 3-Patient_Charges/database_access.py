import os
import sqlite3
from sqlite3 import Error


class Database:

    def create_connection(db_path):
        connection = None
        try:
            connection = sqlite3.connect(db_path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    def generateDatabase(cursor, sql_path):

        sql_files = [f for f in os.listdir(sql_path) if f.endswith(".sql") and
                     f.startswith("0")]
        for file in sql_files:
            print(f"The SQL file {file} is being processed")
            sql_file = open(os.path.join(sql_path, file))
            sql_string = sql_file.read()
            cursor.executescript(sql_string)
            sql_file.close()

    def getAppointment(cursor, sql_path):
        query_path = os.path.join(sql_path, "getQuery.sql")
        sql_file = open(query_path)
        sql_string = sql_file.read()
        cursor.executescript(sql_string)
        sql_file.close()
