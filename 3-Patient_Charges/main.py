import os
from sqlite3 import IntegrityError
from data_handling import Patient, Procedure
from database_access import Database

DB_PATH = os.path.join(os.path.dirname(__file__),
                       "database/hospital_db.sqlite")
SQL_PATH = os.path.join(os.path.dirname(__file__), "database")


def getAllProcedures(procedure_list):
    object_list = []
    for procedure in procedure_list:
        object_list.append(Procedure(*procedure))
    return object_list


def getAllPatients(patient_list, procedure):
    object_list = []
    for patient in patient_list:
        patient.append(procedure)
        object_list.append(Patient(*patient))
    return object_list


def prmntInfo(patient_obj):
    '''Format and prints out the passed object bassed on the classes of 
    Patient and Procedure from data_handling.py
    '''

    print(f"Patient {patient_obj.firstName} {patient_obj.lastName} Data")
    print(f"\t Phone Number: {patient_obj.phoneNumber}")
    print(f"""\t Address: {patient_obj.patientAddress}, \
{patient_obj.patientCity}, {patient_obj.zipCode}\n""")
    print(f"""\t {patient_obj.firstName} {patient_obj.lastName}'s emergency \
contact""")
    print(f"""\t\t Name: {patient_obj.emrgName} Phone Number: \
{patient_obj.ermgPhone}\n""")
    print(f"\t {patient_obj.firstName} {patient_obj.lastName}'s appointments")
    n = 1
    total = 0
    for proc in patient_obj.procedure:
        print(f"\t\t Procedure #{n}:")
        print(f"\t\t Procedure name: {proc.procedureName}")
        print(f"\t\t Date: {proc.procedureDate}")
        print(f"\t\t Doctor: {proc.doctorAssigned}")
        print(f"\t\t Charge: €{proc.procedureFee}\n")
        n += 1
        total += proc.procedureFee
    print(f"\t\t Total procedures charge: €{total}\n")
    print("-" * 90)
    print("\n")


def main():
    '''Executes main function'''

    database = Database()
    connection = database.create_connection(DB_PATH)
    cursor = connection.cursor()
    try:
        with connection:
            database.generateDatabase(cursor, SQL_PATH)
    except IntegrityError as e:
        print(e)

    with connection:
        procedure_list = database.getAppointment(cursor)
        patient_list = database.getPatients(cursor)
    connection.close()

    procedure_objs = getAllProcedures(procedure_list)
    patiente_objs = getAllPatients(patient_list, procedure_objs)
    for obj in patiente_objs:
        prmntInfo(obj)


if __name__ == "__main__":
    main()
