from resources import menu, resources

operate = True
profit = 0


def resources_tank(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def calculate_coins():
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transaction(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        profit += round(money_received - change, 2)
        print(f"Here is your ${change} change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(ingredient):
    for item in ingredient:
        resources[item] -= ingredient[item]
    print(f"Here is your {flavour}. Enjoy!")
    return True


while operate:
    flavour = input("What would you like? (expresso/latte/cappuccino: ")
    if flavour == "off":
        operate = False
    elif flavour == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}gr\n")
        print(f"Profit: ${profit}")
    else:
        drink = menu[flavour]
        if resources_tank(drink["ingredients"]):
            payment = calculate_coins()
            drink_price = drink["cost"]
            if transaction(payment, drink_price):
                make_coffee(drink["ingredients"])
