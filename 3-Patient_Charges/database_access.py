import os
import sqlite3
from sqlite3 import Error


class Database:

    def __init__(self):
        pass

    def create_connection(self, db_path):
        '''Creates and object with the connection to the database.'''
        conn = None
        try:
            conn = sqlite3.connect(db_path)
            print(f"Connection to {os.path.basename(db_path)} successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return conn

    def generateDatabase(self, cursor, sql_path):
        '''With the current connection to DB, gets all files from folder and
         run them as string querys againts the DB.
        '''
        sql_files = [f for f in os.listdir(sql_path) if f.endswith(".sql") and
                     f.startswith("0")]
        for file in sql_files:
            print(f"The SQL file {file} is being processed")
            sql_file = open(os.path.join(sql_path, file))
            sql_string = sql_file.read()
            cursor.executescript(sql_string)
            sql_file.close()

    def getAppointment(self, cursor):
        '''Uses the query to get a list of list with each row of the table
         queried.
         '''

        query_string = """SELECT
        [appointment].[patient_id],
        [appointment].[procedure_name],
        [appointment].[date],
        [doctor].[doctor_name],
        [procedure].[procedure_fee]
        FROM appointment
        INNER JOIN [procedure]
        ON [appointment].[procedure_name] = [procedure].[procedure_name]
        INNER JOIN [doctor]
        ON [appointment].[doctor_id] = [doctor].[doctor_id]"""
        query_result = [list(row) for row in cursor.execute(query_string)]
        return query_result

    def getPatients(self, cursor):
        '''Uses the query to get a list of list with each row of the table
         queried.
        '''

        query_string = """SELECT
        [patient].[patient_id],
        [patient].[first_name],
        [patient].[mid_name],
        [patient].[last_name],
        [patient].[patient_address],
        [patient].[patient_city],
        [patient].[zip_code],
        [patient].[phone_number],
        [patient].[emrg_name],
        [patient].[ermg_phone]
        FROM [patient]"""
        query_result = [list(row) for row in cursor.execute(query_string)]
        return query_result
