# 1 year = 3 days
# 1 year = 52 weeks
# 1 year = 12 month

age = input ("Input your age: ")

yearleft = 90 - int(age)
monthleft = yearleft * 12
weekleft = yearleft * 52
dayleft = yearleft * 365

print(f"you have {dayleft} days, {weekleft} weeks, {monthleft} months left")

