# Mutability
class Student:
    def __init__(self, name: str, grades: list[int] = None):
        self.name = name
        self.grades = grades or []

    def take_examp(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_examp(19)
print(bob.grades)
print(rolf.grades)
