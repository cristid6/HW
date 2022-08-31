# modelam o clasa ce reprezinta un student, dupa care
#o grupa ce reprezita mai multi studenti , iar aceste grupe apartin unui curs

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Group:
    def __init__(self, name, max_number_of_students):
        self.name = name
        self.maxStudents = max_number_of_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.maxStudents:
            self.students.append(student)
            return True
        else:
            return False

    def printStudents(self):
         for student in self.students:
             print(f"Student name:{student.name}")

class Course:
    def __init__(self, name, max_number_of_groups):
        self.name = name
        self.maxGroups = max_number_of_groups
        self.groups = []
        
    def add_group(self, group):
        if len(self.groups) < self.maxGroups:
            self.groups.append(group)
            return True
        else:
            return False
        
    def printGroups(self):
        for group in self.groups:
            print(f"Group name:{group.name}")
