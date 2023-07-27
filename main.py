from data import MENU
from data import resources

order_drink = False
registered_money = 0


def ingredients_remaining(water, milk, coffee):
    return f"water: {water}ml\nmilf: {milk}ml\ncoffee: {coffee}mg"


def menu_select(item):
    global price
    drink = MENU[item]
    price = drink["cost"]
    return price


def buy_drink(quarters, dimes, nickels, pennies, price, resources, item):
    drink = MENU[item]
    ingredients = drink["ingredients"]
    required_water = ingredients["water"]
    required_coffee = ingredients["coffee"]
    if item == "latte" or item == "cappuccino":
        required_milk = ingredients["milk"]
    if resources["water"] < required_water or resources["coffee"] < required_coffee or resources["milk"] < required_milk:
        print("Sorry, the machine has run out of ingredients for this item. Money refunded")
        return False
    else:
        total_amount = float((quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01))
        if total_amount > price:
            change = total_amount - price
            change = round(change, 2)
            money_in_machine = price
            print(f"Here is ${change} in change.\nHere is your {choice}. Enjoy!")
            return True
        if total_amount < price:
            print("Sorry that's not enough money. Money refunded.")
        else:
            return False


def used_ingredients(item, resources, bought_drink):
    drink = MENU[item]
    ingredients = drink["ingredients"]
    water = ingredients["water"]
    coffee = ingredients["coffee"]
    if item == "latte" or item == "cappuccino":
        milk = ingredients["milk"]
    if bought_drink:
        resources["water"] -= water
        resources["coffee"] -= coffee
        if item == "latte" or item == "cappuccino":
            resources["milk"] -= milk


use_coffee_machine = input("Type 'y' to order a drink or type 'n' to exit: ")

if use_coffee_machine == "y":
    order_drink = True

while order_drink:
    choice = input("What would you like?(espresso/latte/cappuccino): ")

    if choice == "report":
        print(ingredients_remaining(resources["water"], resources["milk"], resources["coffee"]))
        print(f"Money: {registered_money}")
    elif choice in MENU:
        print(f"The cost of your drink is {menu_select(choice)}. Please insert coins")
        quarters = float(input("Insert quarters: "))
        dimes = float(input("Insert dimes: "))
        nickels = float(input("Insert nickels: "))
        pennies = float(input("Insert pennies: "))
        bought_drink = buy_drink(quarters, dimes, nickels, pennies, price, resources, choice)
        used_ingredients(choice, resources, bought_drink)
        if bought_drink:
            registered_money += price
