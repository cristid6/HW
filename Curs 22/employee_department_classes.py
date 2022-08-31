"""
Un mic ex: Modelam o clasa ce reprezinta un angajat,
ce are un nume, varsta, salariu
Un departament ce contiune mai multi angajati
pentru departament sa avem optiunea sa adaugam sau
sa scoatem angajati
sa vedem cat cheltuie departemantul pe salarii
"""


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = {}

    def add_employee(self, employee, salary):
        self.employees.update({employee: salary})

    def remove_employee(self, employee):
        del self.employees[employee]
        print(f'Employee {employee} deleted!')

    def print_list_employees(self):
        print(self.employees)

    def print_total_salaries(self):
        print(sum(self.employees.values()))



