from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

items = Menu()
machine_on = True

while machine_on == True:
    options = items.get_items()
    print("Hello! Are you here for some coffee?")
    order = input(f"What would you like? ({options}): ").lower()
    if order == "off":
        print("Goodbye")
        machine_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = items.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
           if money_machine.make_payment(drink.cost):
               coffee_maker.make_coffee(drink)



