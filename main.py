MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 250,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def calculator_coins():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    print('Please insert coins.')
    quarters_user = int(input('how many quarters?: '))
    dimes_user = int(input('how many dimes?: '))
    nickles_user = int(input('how many nickles?: '))
    pennies_user = int(input('how many pennies?: '))
    total_user = quarters_user * quarters + dimes_user * dimes + nickles_user * nickles + pennies_user * pennies
    return total_user


def choose_coffee(user_question, order):
    if total_user >= MENU[user_question]["cost"]:
        rest = round(total_user - MENU[user_question]["cost"], 2)
        resources['money'] += MENU[user_question]["cost"]
        # resources['water'] -= MENU[user_question]["ingredients"]["water"]
        # resources['milk'] -= MENU[user_question]["ingredients"]["milk"]
        # resources['coffee'] -= MENU[user_question]["ingredients"]["coffee"]
        for item in order:
            resources[item] -= order[item]
        print(f"Here is ${rest} in change.")
        print(f"Here is your {user_question} ☕. Enjoy!")
    else:
        print("Sorry that's not enough money!")


def check_resources(user_question):
    # if resources['water'] < MENU[user_question]["ingredients"]["water"]:
    #     print("Sorry there is not enough water")
    #     return True
    # elif resources['milk'] < MENU[user_question]["ingredients"]["milk"] and user_question != 'espresso':
    #     print("Sorry there is not enough milk")
    #     return True
    # elif resources['coffee'] < MENU[user_question]["ingredients"]["coffee"]:
    #     print("Sorry there is not enough coffee")
    #     return True
    for item in user_question:
        if user_question[item] > resources[item]:
            print(f"Sorry there's not enough {item}")
            return True


love_coffee = True

while love_coffee:
    user_question = input('What would you like? (espresso/latte/cappuccino): ').lower()

    # turn off the coffee machine by entering 'off' to the prompt
    # 2.
    if user_question == 'off':
        exit()
    # 3. print report
    elif user_question == 'report':
        for key, value in resources.items():
            print(f"{key.capitalize()}: {value}")
    else:
        # TODO check if there are suffiecient resoucers to make the drink selected
        if check_resources(MENU[user_question]["ingredients"]) == True:
            love_coffee = True
        else:
            # total_user = quarters_user * quarters + dimes_user * dimes + nickles_user * nickles + pennies_user * pennies
            total_user = calculator_coins()
            choose_coffee(user_question,MENU[user_question]["ingredients"])
