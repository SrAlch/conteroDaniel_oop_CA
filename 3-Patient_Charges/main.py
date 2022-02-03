import os
from sqlite3 import IntegrityError
from data_handling import Patient, Procedure
from database_access import Database

DB_PATH = os.path.join(os.path.dirname(__file__),
                       "database/hospital_db.sqlite")
SQL_PATH = os.path.join(os.path.dirname(__file__), "database")

database = Database
connection = database.create_connection(DB_PATH)
cursor = connection.cursor()
try:
    database.generateDatabase(cursor, SQL_PATH)
except IntegrityError as e:
    print(e)
connection.commit()

test = Procedure("Physical exam", "15/09/2021", "Dr Jones", "€300")

patient_list = [list(row) for row in cursor.execute("SELECT * FROM patient")]

connection.close()

args = patient_list[0][1:]
args.append(test)
test_patient = Patient(*args)


'''test_patient = Patient(patient_list[0][1],
                       patient_list[0][2],
                       patient_list[0][3],
                       patient_list[0][4],
                       patient_list[0][5],
                       patient_list[0][6],
                       patient_list[0][7],
                       patient_list[0][8],
                       patient_list[0][9],
                       test)
'''
print(test_patient.emrgName)
