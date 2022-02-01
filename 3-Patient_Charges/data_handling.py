import re
from datetime import datetime


class DataValidation:
    def __init__(self):
        pass

    def nameValidation(self, name):
        regEx_exp = re.match("[A-Za-z\\s]*$", name)
        if regEx_exp:
            return name
        else:
            raise ValueError(f"The name {name} is not a valid one")

    def dateValidation(self, date):
        clean_date = datetime.strptime(date, '%d/%m/%Y')
        return clean_date

    def numberValidation(self, number):
        regEx_exp = re.match("[€+]?[0-9-\\s]*$", number)
        if regEx_exp:
            return number
        else:
            raise ValueError(f"The number {number} is not a valid one")

    def zipValidation(self, zip):
        regEx_exp = re.match("[A-Za-z0-9\\s]*$", zip)
        if regEx_exp:
            return zip
        else:
            raise ValueError(f"The zip code {zip} is not a valid one")


class Procedure(object):
    def __init__(self,
                 procedure_name,
                 procedure_date,
                 doctor_assigned,
                 procedure_fee):

        data = DataValidation
        self.procedure_name = data.nameValidation(self, procedure_name)
        self.procedure_date = data.dateValidation(self, procedure_date)
        self.doctor_assigned = data.nameValidation(self, doctor_assigned)
        self.procedure_fee = data.numberValidation(self, procedure_fee)

    @property
    def procedureName(self):
        return self.procedure_name

    @procedureName.setter
    def procedureName(self, procedure_name):
        self.procedure_name = procedure_name

    @procedureName.deleter
    def procedureName(self):
        del self.procedure_name

    @property
    def procedureDate(self):
        return self.procedure_date

    @procedureDate.setter
    def procedureDate(self, procedure_date):
        self.procedure_date = procedure_date

    @procedureDate.deleter
    def procedureDate(self):
        del self.procedure_date

    @property
    def doctorAssigned(self):
        return self.doctor_assigned

    @doctorAssigned.setter
    def doctorAssigned(self, doctor_assigned):
        self.doctor_assigned = doctor_assigned

    @doctorAssigned.deleter
    def doctorAssigned(self):
        del self.doctor_assigned

    @property
    def procedureFee(self):
        return self.procedure_fee

    @procedureFee.setter
    def procedureFee(self, procedure_fee):
        self.procedure_fee = procedure_fee

    @procedureFee.deleter
    def procedureFee(self):
        del self.procedure_fee


class Patient(Procedure):
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
                 procedure_name,
                 procedure_date,
                 doctor_assigned,
                 procedure_fee):

        data = DataValidation
        self.first_name = data.nameValidation(self, first_name)
        self.mid_name = data.nameValidation(self, mid_name)
        self.last_name = data.nameValidation(self, last_name)
        self.patient_address = patient_address
        self.patient_city = data.nameValidation(self, patient_city)
        self.zip_code = data.zipValidation(self, zip_code)
        self.phone_number = data.numberValidation(self, phone_number)
        self.emrg_name = data.nameValidation(self, emrg_name)
        self.ermg_phone = data.numberValidation(self, ermg_phone)
        Procedure.__init__(self,
                           procedure_name,
                           procedure_date,
                           doctor_assigned,
                           procedure_fee)

    @property
    def firstName(self):
        return self.first_name

    @firstName.setter
    def firstName(self, first_name):
        self.first_name = first_name

    @firstName.deleter
    def firstName(self):
        del self.first_name

    @property
    def midName(self):
        return self.mid_name

    @midName.setter
    def midName(self, mid_name):
        self.mid_name = mid_name

    @midName.deleter
    def midName(self):
        del self.mid_name

    @property
    def lastName(self):
        return self.last_name

    @lastName.setter
    def lastName(self, last_name):
        self.last_name = last_name

    @lastName.deleter
    def lastName(self):
        del self.last_name

    @property
    def patientAddress(self):
        return self.patient_address

    @patientAddress.setter
    def patientAddress(self, patient_address):
        self.patient_address = patient_address

    @patientAddress.deleter
    def patientAddress(self):
        del self.patient_address

    @property
    def patientCity(self):
        return self.patient_city

    @patientCity.setter
    def patientCity(self, patient_city):
        self.patient_city = patient_city

    @patientCity.deleter
    def patientCity(self):
        del self.patient_city

    @property
    def zipCode(self):
        return self.zip_code

    @zipCode.setter
    def zipCode(self, zip_code):
        self.zip_code = zip_code

    @zipCode.deleter
    def zipCode(self):
        del self.zip_code

    @property
    def phoneNumber(self):
        return self.phone_number

    @phoneNumber.setter
    def phoneNumber(self, phone_number):
        self.phone_number = phone_number

    @phoneNumber.deleter
    def phoneNumber(self):
        del self.phone_number

    @property
    def emrgName(self):
        return self.emrg_name

    @emrgName.setter
    def emrgName(self, emrg_name):
        self.emrg_name = emrg_name

    @emrgName.deleter
    def emrgName(self):
        del self.emrg_name

    @property
    def ermgPhone(self):
        return self.ermg_phone

    @ermgPhone.setter
    def ermgPhone(self, ermg_phone):
        self.ermg_phone = ermg_phone

    @ermgPhone.deleter
    def ermgPhone(self):
        del self.ermg_phone


try:
    test = Procedure("Physical exam", "15/09/2021", "Dr Jones", "€300")
except ValueError as e:
    print(e)

print(test.procedureDate)
