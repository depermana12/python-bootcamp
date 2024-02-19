# functions can return another function

def create_adder(x):
    def adder(y):
        return x + y

    return adder

add = create_adder(10)

print(add(5))