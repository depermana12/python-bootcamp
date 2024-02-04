

year = int(input("which year you one to check? "))


# divisible by four
# except every year that evenly divisible by 100
# unless the year is also evenly divisible by 400

check = year % 4
hundredcheck = year % 100
fourhundredcheck = year % 400

if check == 0:
    if hundredcheck == 0: 
        if fourhundredcheck == 0:
            print("leap year")
        else:
            print("not leap")
    else:
        print("leap year")
else:
    print("not leap")
