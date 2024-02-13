class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (100, 100, 100, 90, 99))
average_grade = student.average()

name = student.name
grades = student.grades


print(name)
print(grades)
print(average_grade)
