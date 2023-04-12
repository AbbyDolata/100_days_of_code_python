from coffeeresources import MENU
from coffeeresources import resources

machine_on = True
profit = 0


# TODO: 4. Process coins
def coins():
    """Returns a total after coins have been inserted into the machine"""
    total = 0
    total += int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .10
    total += int(input("How many nickles?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total


def transaction(total):
    """either continues to the process of making coffee or stops transaction after determining if enough money was
    inserted to pay for product"""
    global profit
    if cost > total:
        print("You have not put in the correct amount, here is your money back")
        return False
    elif total == cost:
        profit += cost
        return True
    elif total > cost:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change")
        profit += cost
        return True


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item} to complete your order.")
            return False
    return True


# TODO: 6. Make coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# TODO: 1. Ask users what they want
while machine_on == True:
    print("☕️Hello! Are you here for some coffee?☕️")
    options = input("What would you like?\nEspresso/Latte/Cappuccino/Report/Off: ").lower()
    # TODO: 2. Turn off coffee machine by typing off into prompt
    if options == 'off':
        print("Goodbye")
        machine_on = False
    # TODO: 3. Print report when report is typed into prompt
    # TODO: 8. Make the report available before any drink has been ordered
    # this is an order issue, the order has to come before drinks are ordered, and after
    if options == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        machine_on = False
    if options == "espresso" or options == 'cappuccino' or options == 'latte':
        machine_on = is_resource_sufficient(order_ingredients=MENU[options]['ingredients'])
        if machine_on == True:
            cost = MENU[options]['cost']
            print(f"the cost of your drink will be ${MENU[options]['cost']}")
            machine_on = transaction(coins())
        if machine_on == True:
            make_coffee(drink_name=options, order_ingredients=MENU[options]['ingredients'])
