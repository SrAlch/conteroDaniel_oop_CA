import os
import sqlite3
from sqlite3 import Error

DB_PATH = os.path.join(os.path.dirname(__file__),
                       "database/hospital_db.sqlite")
DB_FILES_PATH = os.path.join(os.path.dirname(__file__),
                             "database")


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def runAllSQL(cursor):

    sql_files = [f for f in os.listdir(DB_FILES_PATH) if f.endswith(".sql")]
    for file in sql_files:
        print(file)
        sql_file = open(os.path.join(DB_FILES_PATH, file))
        sql_string = sql_file.read()
        cursor.executescript(sql_string)
        sql_file.close()


connection = create_connection(DB_PATH)
cursor = connection.cursor()
runAllSQL(cursor)
connection.commit()
connection.close()
