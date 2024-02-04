

inputnumber = int(input("please enter a number: "))


def prime_checker(number):
    if number > 1:
        for count in range(2, number):
            if number % count == 0:
                print("It's not prime number")
                break
            else:
                print("It's prime number")
                break
    else:
        print("It's not a prime number")


prime_checker(inputnumber)
