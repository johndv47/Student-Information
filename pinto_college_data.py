"""
script: pinto_college_data.py
action: a. Reads employee and student data from employees.txt and students.txt
        b. Employee and Student class inherits from ABC Person class.
        c. Displays employment information and contact information.
        d. Displays student and all persons contact information.
        e. Validates employee classification and role via dictionary keys.
        f. Validates annual salary is a non-negative value.

NOTE: employees.txt and students.txt were directly downloaded from the project instructions.
      File was parsed based on original formatting.

author: John Pinto
date: 4/27/2026
"""
# View comment in createMenu() function if 'ERROR: employees.txt not found.' is displayed in the menu.
#import os
from datetime import date
from abc import ABC, abstractmethod

# Both Employees and Student objects are appended to personList to keep track
# of total persons.




## UPDATE CODE TO RETURN EMPLOYEE / STUDENTS AS OBJECTS - THIS WILL INCREASE MODULARITY FUNCTIONALITY

# REWRITE PERSON LIST INTO MAIN INIT
personList = []

class Person(ABC):
    """
    Person is an abstract base class. You will not be able to create an object of this
    class. Employee inherits from this person base class.
    """
    @abstractmethod
    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber):
        self._firstName = firstName
        self._lastName = lastName
        self._idNumber = idNumber
        self._emailAddress = emailAddress
        self._phoneNumber = phoneNumber

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        self._firstName = value

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        self._lastName = value

    @property
    def idNumber(self):
        return self._idNumber

    @property
    def emailAddress(self):
        return self._emailAddress

    @emailAddress.setter
    def emailAddress(self, value):
        self._emailAddress = value

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, value):
        self._phoneNumber = value

    # Individual person details - formatted for debugging purposes.
    def __repr__(self):
        return(
            f"Last Name: {self._lastName}\n"
            f"First Name: {self._firstName}\n"
            f"ID: {self._idNumber}\n"
            f"Email Address: {self._emailAddress}\n"
            f"Phone Number: {self._phoneNumber}\n"
            )

    # String representation of individual person - formatted for end-user display
    def __str__(self):
        return (
            f"{self._firstName} {self._lastName} | ID: {self._idNumber} | "
            f"{self._emailAddress} | {self._phoneNumber}"
        )


class Employee(Person):
    """
    Employee inherits from abstract class, Person.
    roleDictionary and classificationDictionary act as keys to decode
    faculty, staff, full-time, and part-time.
    """

    roleDictionary = {"001": "Staff", "002": "Faculty"}
    classificationDictionary = {"001": "Full-Time", "002": "Part-Time"}

    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber,
                 hireDate, rolePerson, classificationPerson, annualSalary):

        # Initializes variables from Person class.
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)

        # hireDate in tuple - using datetime module
        self._hireDate = date(hireDate[2], hireDate[0], hireDate[1])
        
        # Validates employee's role (e.g. Staff or Faculty)
        if rolePerson not in Employee.roleDictionary:
            raise ValueError(f"Invalid role: '{rolePerson}'. Role must be one of the following{Employee.roleDictionary}")
        self._rolePerson = rolePerson
        
        # Validates employee's classification key (e.g. Full-Time, Part-Time)
        if classificationPerson not in Employee.classificationDictionary:
            raise ValueError(f"Invalid classification: '{classificationPerson}'. Classification must be one of the following {Employee.classificationDictionary}.")
        self._classificationPerson = classificationPerson

        # Validates annual salary is not negative
        if annualSalary < 0:
            raise ValueError(f"Salary can ONLY be non-negative.")
        self._annualSalary = annualSalary

    @property
    def hireDate(self):
        return self._hireDate

    @property
    def rolePerson(self):
        return self._rolePerson

    @rolePerson.setter
    def rolePerson(self, value):
        if value not in Employee.roleDictionary:
            raise ValueError(f"Invalid role: '{value}'. Role must be one of the following{Employee.roleDictionary}")
        self._rolePerson = value

    @property
    def classificationPerson(self):
        return self._classificationPerson

    @classificationPerson.setter
    def classificationPerson(self, value):
        if value not in Employee.classificationDictionary:
            raise ValueError(f"Invalid classification: '{value}'. Classification must be one of the following {Employee.classificationDictionary}")
        self._classificationPerson = value

    @property
    def annualSalary(self):
        return self._annualSalary

    @annualSalary.setter
    def annualSalary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._annualSalary = value



    # Employee details - formatted for debugging purposes.
    def __repr__(self):
        # Sets role and classification from Employee's class methods roleDictionary & classificationDictionary
        role = Employee.roleDictionary[self._rolePerson]
        classification = Employee.classificationDictionary[self._classificationPerson]
        return(
            f"Last Name: {self._lastName}\n"
            f"First Name: {self._firstName}\n"
            f"ID: {self._idNumber}\n"
            f"Email Address: {self._emailAddress}\n"
            f"Phone Number: {self._phoneNumber}\n"
            f"Hire Date: {self._hireDate.strftime('%m/%d/%Y')}\n"
            f"Role: {role}\n"
            f"Classification: {classification}\n"
            f"Salary: ${self._annualSalary:.2f}\n"
        )


    # String representation of employee - formatted for end-user display
    def __str__(self):
        # Sets role and classification from Employee's class methods roleDictionary & classificationDictionary
        role = Employee.roleDictionary[self._rolePerson]
        classification = Employee.classificationDictionary[self._classificationPerson]
        return (
            f"{self._firstName} {self._lastName} | ID: {self._idNumber} | "
            f"{self._emailAddress} | {self._phoneNumber} | "
            f"{self._hireDate.strftime('%m/%d/%Y')} | {role} | {classification} | ${self._annualSalary:.2f}"
        )


class Student(Person):
    """
    Student inherits from abstract class, Person.
    """

    def __init__(self, firstName, lastName, idNumber, emailAddress, phoneNumber):
        # Initializes variables from Person class.
        super().__init__(firstName, lastName, idNumber, emailAddress, phoneNumber)


    # Student details - formatted for debugging purposes.
    def __repr__(self):
        return(
            f"Last Name: {self._lastName}\n"
            f"First Name: {self._firstName}\n"
            f"ID: {self._idNumber}\n"
            f"Email Address: {self._emailAddress}\n"
            f"Phone Number: {self._phoneNumber}\n"
        )


    # String representation of student - formatted for end-user display
    def __str__(self):
        return (
            f"{self._firstName} {self._lastName} | ID: {self._idNumber} | "
            f"{self._emailAddress} | {self._phoneNumber}"
        )


# FILE HANDLING - Employees
# employees.txt is required to call this function
def getEmployees():
        employeeList = []
    try:
        with open('employees.txt', 'r') as file:
            next(file) # Skips header line
            for line in file:
                # Creates a field that strips every tab from the formatted .txt file.
                fields = [f.strip() for f in line.split('\t') if f.strip() != '']


                # Assigns employee variables to desired fields
                lastName = fields[0]
                firstName = fields[1]
                idNumber = int(fields[2])
                emailAddress = fields[3]
                phoneNumber = fields[4]
                hireDateStr = fields[5] 
                classificationVal = fields[6]
                roleVal = fields[7]
                annualSalary = float(fields[8])


                # Hire date formatted into parts. (month/day/year) is represented as tuple
                hireParts = hireDateStr.split('/')
                hireDate = (int(hireParts[0]), int(hireParts[1]), int(hireParts[2]))

                # Used to validate key in classificationDictionary
                classificationLookup = classificationVal + "-Time"
                classificationKey = None
                for key, val in Employee.classificationDictionary.items():
                    if classificationLookup == val:
                        classificationKey = key
                        break

                if classificationKey is None:
                    print(f"Skipping {firstName} {lastName}: invalid classification '{classificationVal}'")
                    continue


                roleKey = None
                for key, val in Employee.roleDictionary.items():
                    if roleVal == val:
                        roleKey = key
                        break

                if roleKey is None:
                    print(f"Skipping {firstName} {lastName}: invalid role '{roleVal}'")
                    continue

                # Appends Employee as an object to employeeList and personList
                employeeList.append(Employee(firstName, lastName, idNumber, emailAddress, phoneNumber,
                                            hireDate, roleKey, classificationKey, annualSalary))
                personList.append(Employee(firstName, lastName, idNumber, emailAddress, phoneNumber,
                                            hireDate, roleKey, classificationKey, annualSalary))

                print(f"Added employee {firstName} {lastName}...")

    except FileNotFoundError:
        # employees.txt needs to be in CWD and not in a subfolder.
        print("ERROR: employees.txt not found.")


# Displaying Information
def displayEmployeeInformation():
    """
    Displays first name, last name, ID, email, phone number, hire date, classification,
    role, and salary headers.
    """
    print(f"\n{'Employment Information':^125}\n")
    print(f"{'LastName':<15}{'FirstName':<12}{'ID':<6}"
          f"{'Email':<32}{'Phone':<15}"
          f"{'HireDate':<14}{'Classification':<16}{'Role':<10}{'Salary':>7}")
    print("-" * 131)

    # Assigns role and classification to each employee object (iterates employeeList)
    for emp in employeeList:
        role = Employee.roleDictionary[emp.rolePerson]
        classification = Employee.classificationDictionary[emp.classificationPerson]
        # Separates Full-Time to Full & Part-Time to Part
        short_classification = classification.split("-")[0]
        hireDateStr = f"{emp.hireDate.month}/{emp.hireDate.day}/{emp.hireDate.year}"

        print(
            f"{emp.lastName:<15}{emp.firstName:<12}{emp.idNumber:<6}"
            f"{emp.emailAddress:<32}{emp.phoneNumber:<15}"
            f"{hireDateStr:<14}{short_classification:<16}{role:<10}{emp.annualSalary:>9.2f}"
            )
        print()


def displayEmployeeContact():
    """Print a formatted contact information report."""
    print(f"\n{'Employee Contact Information':^80}\n")
    print(
        f"{'LastName':<15}{'FirstName':<12}{'ID':<6}"
        f"{'Email':<35}{'Phone':<15}"
    )
    print("-" * 82)

    # Iterates employeeList, displaying Employee contact information.
    for emp in employeeList:
        print(
            f"{emp.lastName:<15}{emp.firstName:<12}{emp.idNumber:<6}"
            f"{emp.emailAddress:<35}{emp.phoneNumber:<15}"
        )
    print()


# FILE HANDLING - Students



def getStudents():
        studentList = []
    try:
        with open('students.txt', 'r') as file:
            next(file)
            for line in file:
                # Creates a field that strips every tab from the formatted .txt file.
                fields = [f.strip() for f in line.split('\t') if f.strip() != '']

                # Assigns Student variables to desired fields
                lastName = fields [0]
                firstName = fields[1]
                idNumber = int(fields[2])
                emailAddress = fields[3]
                phoneNumber = fields[4]



                # Appends Student as an object to the studentList and personList
                studentList.append(Student(firstName, lastName, idNumber, emailAddress, phoneNumber))
                personList.append(Student(firstName, lastName, idNumber, emailAddress, phoneNumber))

                print(f"Added student {firstName} {lastName}...")


    except FileNotFoundError:
        # students.txt needs to be in CWD and not in a subfolder.
        print("ERROR: students.txt not found.")


def displayStudentContact():
    """
    Displays first name, last name, ID, email, phone number for students.
    """
    print(f"\n{'Student Contact Information':^75}\n")
    print(f"{'LastName':<15}{'FirstName':<12}{'ID':<6}"
          f"{'Email':<32}{'Phone':<15}"
    )
    print("-" * 80)

    # Iterates studentList and prints in the formatted table
    for student in studentList:
        print(
            f"{student.lastName:<15}{student.firstName:<12}{student.idNumber:<6}"
            f"{student.emailAddress:<32}{student.phoneNumber:<15}"
              )
        print()


def displayAllPersonsContact():
    """
    Displays first name, last name, ID, email, and phone number
    for all Persons.
    """
    print(f"\n{'All Persons Contact Information':^75}\n")
    print(f"{'LastName':<15}{'FirstName':<12}{'ID':<6}"
          f"{'Email':<32}{'Phone':<15}"
    )
    print("-" * 80)

    # Iterates personList and prints in the formatted table
    for person in personList:
        print(
            f"{person.lastName:<15}{person.firstName:<12}{person.idNumber:<6}"
            f"{person.emailAddress:<32}{person.phoneNumber:<15}"
            )
        print()



# Menu
def createMenu():
    while True:
        # NOTE: Enable this line to view CWD. The employees.txt file must
        # be in the current working directory and not in a subdirectory.
        #print("CWD: ", os.getcwd())
        print("=" * 45)
        print("=             College Data                  =")
        print("=                System                     =")
        print("=" * 45)
        print("\n1. Quit")
        print("2. Display Employee Employment Information")
        print("3. Display Employee Contact Information")
        print("4. Display Student Contact Information")
        print("5. Display All Persons Contact Information")
        selection = input("Please select 1-5: ")

        try:
            # Converts selection to int value in order to validate menu selection.
            selection = int(selection)
        except ValueError:
            print("\nERROR: Only enter a number that is 1-5. Try again.\n")
            continue

        if selection == 1:
            print("\nExiting the program...")
            exit()

        elif selection == 2:
            displayEmployeeInformation()

        elif selection == 3:
            displayEmployeeContact()

        elif selection == 4:
            displayStudentContact()

        elif selection == 5:
            displayAllPersonsContact()

        else:
            print("\nERROR: Only enter a number that is 1-5. Try again.\n")


# Initiates program.
if __name__ == "__main__":
    print("Starting College Data System...\n")
    print("Adding employees...")
    getEmployees()
    print("Adding students...")
    getStudents()
    print()
    #for emp in employeeList:
    #    print(emp)
    #    print()
    #for student in studentList:
    #    print(student)
    #    print()
    #for person in personList:
    #    print(person)
    #    print()
    createMenu()
