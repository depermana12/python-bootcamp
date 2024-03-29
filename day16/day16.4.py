from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

operate = True

# create object COFFEE_MAKER from class blueprint CoffeeMaker()
coffee_maker = CoffeeMaker()
menu = Menu()
cashier = MoneyMachine()


while operate:
    # assigning object menu with get_items method
    options = menu.get_items()
    flavour = input("What would you like? (expresso/latte/cappuccino: ")
    if flavour == "off":
        operate = False
    elif flavour == "report":
        coffee_maker.report()
        cashier.report()
    else:
        drink = menu.find_drink(flavour)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if cashier.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
