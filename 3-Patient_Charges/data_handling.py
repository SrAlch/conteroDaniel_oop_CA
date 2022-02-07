import re
from datetime import datetime


class DataValidation:
    def __init__(self):
        pass

    def nameValidation(self, name):
        '''Checks with regular expresions.'''

        regEx_exp = re.match("[A-Za-z-\\s]*$", name)
        if regEx_exp:
            return name
        else:
            raise ValueError(f"The name {name} is not a valid one")

    def dateValidation(self, date):
        '''Gets the inputed string and trys to match the date patern to return
         a time object.
        '''

        clean_date = datetime.strptime(date, '%d-%m-%Y')
        return clean_date

    def numberValidation(self, number):
        '''Gets the number frm the input, check that is a number with the
         allowed symbols and returns a string.
        '''

        regEx_exp = re.match("[€+]?[0-9-\\s]*$", str(number))
        if regEx_exp:
            return number
        else:
            raise ValueError(f"The number {number} is not a valid one")

    def zipValidation(self, zip):
        '''Gets the number frm the input, check that is a number with the
         allowed symbols and returns a string.
        '''

        regEx_exp = re.match("[A-Za-z0-9-\\s]*$", zip)
        if regEx_exp:
            return zip
        else:
            raise ValueError(f"The zip code {zip} is not a valid one")

    def __listCleaner(self, input):
        '''Checks if the input is a list with instances or an instance of the
         class Procedure, then returns a new list with the instances.
        '''

        output_list = []
        if isinstance(input, list):
            checked = []
            for i in input:
                if isinstance(i, Procedure):
                    checked.append(i)
            output_list = checked
        elif isinstance(input, Procedure):
            output_list = [input]
        return output_list

    def checkProcedureInstance(self, object_list):
        '''Generates a valid list from the inputed object, checks if is a valid
         procedure and returns the result.
        '''

        object_list = self.__listCleaner(object_list)
        output_list = []
        for object in object_list:
            if isinstance(object, Procedure):
                output_list.append(object)
            else:
                raise ValueError("The procedure inputed is not a valid object")
        return output_list


class Procedure():
    '''Initializes the class Procedure with the needed values. Each one of them
     is validated on input and on later updates of the value on the decorators.
    '''

    def __init__(self,
                 procedure_name,
                 procedure_date,
                 doctor_assigned,
                 procedure_fee):

        self.__data = DataValidation()
        self.__procedure_name = self.__data.nameValidation(procedure_name)
        self.__procedure_date = self.__data.dateValidation(procedure_date)
        self.__doctor_assigned = self.__data.nameValidation(doctor_assigned)
        self.__procedure_fee = self.__data.numberValidation(procedure_fee)

    @property
    def procedureName(self):
        return self.__procedure_name

    @procedureName.setter
    def procedureName(self, procedure_name):
        self.__procedure_name = self.__data.nameValidation(procedure_name)

    @procedureName.deleter
    def procedureName(self):
        del self.__procedure_name

    @property
    def procedureDate(self):
        return self.__procedure_date

    @procedureDate.setter
    def procedureDate(self, procedure_date):
        self.__procedure_date = self.__data.dateValidation(procedure_date)

    @procedureDate.deleter
    def procedureDate(self):
        del self.__procedure_date

    @property
    def doctorAssigned(self):
        return self.__doctor_assigned

    @doctorAssigned.setter
    def doctorAssigned(self, doctor_assigned):
        self.__doctor_assigned = self.__data.nameValidation(doctor_assigned)

    @doctorAssigned.deleter
    def doctorAssigned(self):
        del self.__doctor_assigned

    @property
    def procedureFee(self):
        return self.__procedure_fee

    @procedureFee.setter
    def procedureFee(self, procedure_fee):
        self.__procedure_fee = self.__data.numberValidation(procedure_fee)

    @procedureFee.deleter
    def procedureFee(self):
        del self.__procedure_fee


class Patient:
    '''Initializes the class Patient with the needed values. Each one of them
     is validated on input and on later updates of the value on the decorators.
    '''

    def __init__(self,
                 first_name,
                 mid_name,
                 last_name,
                 patient_address,
                 patient_city,
                 zip_code,
                 phone_number,
                 emrg_name,
                 ermg_phone,
                 procedure):

        self.__data = DataValidation()
        self.__first_name = self.__data.nameValidation(first_name)
        self.__mid_name = self.__data.nameValidation(mid_name)
        self.__last_name = self.__data.nameValidation(last_name)
        self.__patient_address = patient_address
        self.__patient_city = self.__data.nameValidation(patient_city)
        self.__zip_code = self.__data.zipValidation(zip_code)
        self.__phone_number = self.__data.numberValidation(phone_number)
        self.__emrg_name = self.__data.nameValidation(emrg_name)
        self.__ermg_phone = self.__data.numberValidation(ermg_phone)
        self.__procedure = self.__data.checkProcedureInstance(procedure)

    @property
    def firstName(self):
        return self.__first_name

    @firstName.setter
    def firstName(self, first_name):
        self.__first_name = self.__data.nameValidation(first_name)

    @firstName.deleter
    def firstName(self):
        del self.__first_name

    @property
    def midName(self):
        return self.__mid_name

    @midName.setter
    def midName(self, mid_name):
        self.__mid_name = self.__data.nameValidation(mid_name)

    @midName.deleter
    def midName(self):
        del self.__mid_name

    @property
    def lastName(self):
        return self.__last_name

    @lastName.setter
    def lastName(self, last_name):
        self.__last_name = self.__data.nameValidation(last_name)

    @lastName.deleter
    def lastName(self):
        del self.__last_name

    @property
    def patientAddress(self):
        return self.__patient_address

    @patientAddress.setter
    def patientAddress(self, patient_address):
        self.__patient_address = patient_address

    @patientAddress.deleter
    def patientAddress(self):
        del self.__patient_address

    @property
    def patientCity(self):
        return self.__patient_city

    @patientCity.setter
    def patientCity(self, patient_city):
        self.__patient_city = self.__data.nameValidation(patient_city)

    @patientCity.deleter
    def patientCity(self):
        del self.__patient_city

    @property
    def zipCode(self):
        return self.__zip_code

    @zipCode.setter
    def zipCode(self, zip_code):
        self.__zip_code = self.__data.zipValidation(zip_code)

    @zipCode.deleter
    def zipCode(self):
        del self.__zip_code

    @property
    def phoneNumber(self):
        return self.__phone_number

    @phoneNumber.setter
    def phoneNumber(self, phone_number):
        self.__phone_number = self.__data.numberValidation(phone_number)

    @phoneNumber.deleter
    def phoneNumber(self):
        del self.__phone_number

    @property
    def emrgName(self):
        return self.__emrg_name

    @emrgName.setter
    def emrgName(self, emrg_name):
        self.__emrg_name = self.__data.nameValidation(emrg_name)

    @emrgName.deleter
    def emrgName(self):
        del self.__emrg_name

    @property
    def ermgPhone(self):
        return self.__ermg_phone

    @ermgPhone.setter
    def ermgPhone(self, ermg_phone):
        self.__ermg_phone = self.__data.numberValidation(ermg_phone)

    @ermgPhone.deleter
    def ermgPhone(self):
        del self.__ermg_phone

    @property
    def procedure(self):
        return self.__procedure

    @procedure.setter
    def procedure(self, procedure):
        self.__procedure = self.__procedure.extend(
            self.__data.checkProcedureInstance(procedure))

    @procedure.deleter
    def procedure(self):
        del self.__procedure
        self.__procedure = []
