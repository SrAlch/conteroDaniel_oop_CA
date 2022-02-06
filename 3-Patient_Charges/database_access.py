import os
import sqlite3
from sqlite3 import Error


class Database:

    def __init__(self):
        pass

    def create_connection(self, db_path):
        ''''''
        conn = None
        try:
            conn = sqlite3.connect(db_path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return conn

    def generateDatabase(self, cursor, sql_path):
        ''''''
        sql_files = [f for f in os.listdir(sql_path) if f.endswith(".sql") and
                     f.startswith("0")]
        for file in sql_files:
            print(f"The SQL file {file} is being processed")
            sql_file = open(os.path.join(sql_path, file))
            sql_string = sql_file.read()
            cursor.executescript(sql_string)
            sql_file.close()

    def getAppointment(self, cursor):
        ''''''
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
        ''''''
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
