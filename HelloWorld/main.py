import game_data

menu = game_data.MENU
resources = game_data.resources
profit = 0


def enough_resources(drink):
    # If the drink needs an ingredient AND that ingredient isn't present then return false(not enough resources)
    # Also prints out and subtracts resources used

    for ingredient in drink["ingredients"]:
        if ingredient in drink["ingredients"] and resources[ingredient] < drink["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            resources[ingredient] -= drink["ingredients"][ingredient]

    return True


def process_coins(drink):
    # Gets cost of drink
    cost = drink["cost"]

    # Asks for the number of each denomination of coin

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    # Calculates total amount put into machine
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print("Here is ${:.2f} in change.".format(total - cost))
        return cost


def coffee_machine():
    # Defining needed variables
    global profit
    choice = ""

    # Get customer choice

    choice = input("What would you like? (espresso, latte, cappuccino): ").lower()

    if choice == "off":
        print("Shutting down...")
        return

    # Checks if there is enough resources and proceeds to make the drink
    if choice == "report":
        print("Water: {}ml\nMilk: {}ml\nCoffee: {}g\nMoney: ${}".format(resources["water"], resources["milk"], resources["coffee"], profit))
    elif not(choice == "espresso" or choice == "latte" or choice == "cappuccino"):
        print("Wrong input")
    elif enough_resources(menu[choice]):
        # Processes coins for the drink and adds them to profit
        profit = process_coins(menu[choice])
        print(f"Here's your {choice}, Enjoy!")

    # Recursion
    coffee_machine()

coffee_machine()
