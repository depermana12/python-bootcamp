class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # str method turn an object into string, such as printing object blueprint
    def __str__(self):
        return f"Person {self.name}, {self.age}"

    # use to print unambiguous representation of an object
    def __repr__(self):
        return f"<Person {self.name}, {self.age}>"


bob = Person("Bob", 35)
print(bob)