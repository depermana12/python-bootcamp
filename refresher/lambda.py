numbers = [1, 2, 4, 6, 8, 10]
def double_func(x):
    return x * 2

doubled_first = [double_func(x) for x in numbers]
print(doubled_first)

doubled_map = list(map(double_func, numbers))
print(doubled_map)

doubled_lambda = [(lambda x: x * 3)(x) for x in numbers]
print(doubled_lambda)

# literal map return map object address, use list to return the value
doubled_lambda_map = list(map(lambda x: x * 10, numbers))
print(doubled_lambda_map)