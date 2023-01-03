from coffeeData import MENU, resources, coins
import sys


# Extension of input for system codes "off", "report"
def input_extended(question):
    answer = input(question)
    if answer == "off":
        print("======= OFF =======")
        sys.exit(0)
    elif answer == "report":
        for rsc_name in resources:
            print(f"{rsc_name}: {resources[rsc_name]}ml")
        return input_extended(question)
    else:
        return answer


# Check resources sufficient
def is_sufficient(order):
    """Check any depleted resources and return the list of depleted resources.
    Otherwise, compare the given order's required resources with the resources remained."""
    depleted_rsc = []
    for rsc_name in resources:
        if resources[rsc_name] == 0:
            depleted_rsc.append(rsc_name)
    if len(depleted_rsc) > 0:
        return depleted_rsc

    ingredients = MENU[order]["ingredients"]
    for required_rsc_name in ingredients:
        if resources[required_rsc_name] < ingredients[required_rsc_name]:
            depleted_rsc.append(required_rsc_name)
    return depleted_rsc


def process_coins(order, balance):
    transaction_success = False
    def should_continue(remain):
        if remain > 0:
            return True
        elif remain < 0:
            print(f"Here is ${-remain} dollars in change.")
        return False

    cost = MENU[order]["cost"]

    # Insert coin from quarters to pennies and check if the money is enough
    for coin in coins:
        number_coins = int(input_extended(f"How many {coin}?: "))
        cost -= number_coins * coins[coin]
        if not should_continue(cost):
            balance += cost
            transaction_success = True
            return transaction_success

    if cost > 0:
        print(f"Sorry that's not enough money. Money refunded.")
        transaction_success = False
        return transaction_success

    return transaction_success


def make_coffee(order):
    required_rsc = MENU[order]["ingredients"]
    for rsc_name in required_rsc:
        resources[rsc_name] -= required_rsc[rsc_name]


# Run Coffee machine
def run_coffee_machine():
    balance = 0
    while True:
        # Ask user's order
        order = input_extended("What would you like? (espresso/latte/cappuccino): ")
        # Check whether there is insufficient resources
        depleted_rsc = is_sufficient(order)
        if len(depleted_rsc) > 0:
            for rsc_name in depleted_rsc:
                print(f">> Sorry there is not enough {rsc_name}")
        else:
            # Process Coins
            transaction_success = process_coins(order, balance)
            if transaction_success:
                # Make Coffee
                make_coffee(order)
                print(f">> Here is your {order}. Enjoy!!")


run_coffee_machine()
