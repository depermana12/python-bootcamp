# dictionary unpacking, return dictionary with 2 keyword arguments
# ** collect named arguments into dictionary
def named(**kwargs):
    print(kwargs)

print(named(name="Bob", age=25))

def named_argument(name, age, gender):
    return(name, age, gender)

person = {"name": "Bob", "age": 30, "gender": "male"}
# using ** in function call, unpack dictionary into named arguments
print(named_argument(**person))

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

"""
syntax *args and **kwargs is normally used to accept unlimited number
of argument.
* you got tuple of argument
** you got a dictionaries
"""
def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bober", age=25)
print(both)