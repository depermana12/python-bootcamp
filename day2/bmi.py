
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

intHeight = float(height)
intWeight = int(weight)

bmi = intWeight / (intHeight**2)


print(round(bmi))