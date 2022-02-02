import os
from sqlite3 import IntegrityError
from data_handling import Patient
from database_access import Database

DB_PATH = os.path.join(os.path.dirname(__file__),
                       "database/hospital_db.sqlite")
SQL_PATH = os.path.join(os.path.dirname(__file__), "database")

database = Database
connection = database.create_connection(DB_PATH)
cursor = connection.cursor()
try:
    database.runAllSQL(cursor, SQL_PATH)
except IntegrityError as e:
    print(e)

connection.commit()
for row in cursor.execute("SELECT * FROM patient"):
    print(list(row))

connection.close()
