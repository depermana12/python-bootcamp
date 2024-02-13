def mutiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg

    return total

print(mutiply(1, 2, 7))

def add(x, y):
    return x + y

nums = [3, 7]
addition = add(*nums)
print(addition)

numbers = {"x": 6, "y": 6}
dict_addition = add(**numbers)
print(dict_addition)
