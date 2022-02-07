Class assignment from DBS (Dublin Business School) for Object Oriented Programming

Added SQL database to practice Database connection

# Assessment Specification**

## 1. Reads Data and Plots.

Create a Text File that contains your expenses for the last month in the following categories:

- Rent
- Gas
- Food
- Clothing
- Car Payments
- Misc

Write a python program that reads the Data from the file and uses matplotlib to plot a pie chart showing how you spent your money.

## 2. Word Index.

Write a program that reads the contents of a text file. The program should create a dictionary in which the key-pairs are described as follows:

- Key: The keys are the individual words found in the file.
- Values: Each value is a list that contains the line numbers in the file where the word {key} is found.

Example, suppose the word  'robot' is found in lines 7,18,94, and 138. The dictionary would contain an element in which the key was the string 'robot' , and the value was a list containing the numbers 7,18,94,138.

Once the dictionary is built the program should create another text file, known as a word index, listing the contents of the dictionary. The word index file should contain an alphabetical listing of the words that are stored as keys in the dictionary, along with the line numbers where the words appear in the original file.

## 3. Patient Charges.

Write a class called Patient that has the following attributes for the following data:

- First Name, Middle Name, and Last Name
- Address, City, ZIP Code
- Phone Number
- Name and Phone Number of Emergency contact

The Patients class's__init__ method should accept an argument for each attribute.

The Patient class should also have accessor and mutator methods for each attribute.

Next write a class called Procedure that represents a medical procedure that has been performed on a patient. The procedure class should have attributes for the following data:

- Name of Procedure
- Date of procedure
- Name of the Doctor who performed the procedure
- Charges for the procedure

The procedure class's__init__ method should accept an argument for each attribute.

The procedure class should also have accessor and mutator methods for each attribute.

Next write a program that creates an instance of the Patient class, initialized with sample data. Then, create 3 instances of the procedure class initializing with the following data:

#### Procedure #1
>Procedure name: Physical exam
Date: 15/09/2021
Doctor: Dr Jones
Charge: €300

#### Procedure #2
>Procedure name: X-Ray
Date: 15/09/2021
Doctor: Dr Ryan
Charge: €600

#### Procedure #3
>Procedure name: Blood Test
Date: 15/09/2021
Doctor: Dr Smith
Charge: €100

The program should display the patient's information, information about all 3 of the procedures, and the total charges of the 3 procedures.