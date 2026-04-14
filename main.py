"""
script: emp.py
action: a.
        b.
        c.
        d.
author: John Pinto
date: 3/26/2026
"""

#import os
from datetime import date
from abc import ABC, abstractmethod


class Person(ABC):
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

    @property
    def lastName(self):
        return self._lastName

    @property
    def idNumber(self):
        return self._idNumber

    @property
    def emailAdress(self):
        return self._emailAddress

    @property
    def phoneNumber(self):
        return self._phoneNumber

    def __rpr__(self):
        return (
            f"First name: {self.firstName}\n"
            f"Last name: {self.lastName}\n"
            f"ID number: {self.idNumber}"
            f"Email address: {self.emailAdress}"
            f"Phone number: {self.phoneNumber}"
        )


class Student(Person):
    def __init__(
        self,
        firstName,
        lastName,
        idNumber,
        emailAdress,
        phoneNumber,
    ):

        super().__init__(firstName, lastName, idNumber, emailAdress, phoneNumber)

        self._hireDate = hireDate
        self._rolePerson = rolePerson
        self._classificationPerson = classificationPerson
        self._annualSalary = annualSalary

        def __repr__(self):
        def __str__(self):

        


def main():
    while True:
        print("Add emp")
        print("Edit emp")
        print("Delete emp")
        selection = input("Please select 1-3: ")

        try:
            selection = int(selection)
        except ValueError:
            print("Enter a number")
            continue

        if selection == 1:
            add()
        elif selection == 2:
            edit()
        elif selection == 3:
            delete()
        else:
            print("wrong")


if __name__ == "__main__":
    main()
