"""
Tema:
Class Person de baza
O clasa angajat ce mosteste din person
O clasa Manager ce mostenste din person
Ca proprietati care sunt la fel (nume, varsta, etc)
Dar au diferit nivelul de acces intr-o aplicatie sau companie
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

class Employee(Person):
    def __init__(self, name, age, rank_access):
        super().__init__(name, age)
        self.rank_access = rank_access
        
        
class Manager(Person):
    def __init__(self, name, age, rank_access):
        super().__init__(name, age)
        self.rank_access = rank_access
