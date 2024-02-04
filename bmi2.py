
height = float(input("enter your height in cm: "))
wheight = float(input("enter your weight in kg: "))

heightInM = height / 100
bmi = wheight / heightInM ** 2
bmiround = round(bmi, 1)

print(bmiround)

if bmiround <= 18.5:
    print("you are underweight")
elif bmiround < 25:
    print("you have a normal weight")
elif bmiround < 30:
    print("you are overweight")
elif bmiround  < 35:
    print("you are obese")
else:
    print("you are clinically obese")