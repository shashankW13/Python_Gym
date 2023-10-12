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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

currency_values = {
    'quarter': 0.25,
    'dime': 0.10,
    'nickel': 0.05,
    'penny': 0.01,
}

run_coffee_machine = True


def report(available_resources):
    for resource, quantity in resources.items():
        print(f'{resource}: {quantity}' +
              ('g' if resource == 'coffee'
               else '$' if resource == 'money'
              else 'ml'))


def check_resources(serving):
    # print(serving)
    for item in serving:
        # print(item)
        if resources[item] < serving[item]:
            print(f"Sorry not enough {item}")
            return False
        else:
            return True


def prepare_coffee(coffee):
    # print(coffee)
    for item in coffee['ingredients']:
        # print(item)
        resources[item] -= coffee['ingredients'][item]
    resources['money'] += coffee['cost']
    print(f'\nCoffee prepared, Here\'s your {coffee}!\n')

def coin_calculator(quarter, dime, nickel, penny, coffee):
    coffee_cost = MENU[coffee]['cost']
    quarter_value = currency_values['quarter'] * quarter
    dime_value = currency_values['dime'] * dime
    nickel_value = currency_values['nickel'] * nickel
    penny_value = currency_values['penny'] * penny

    total_cost = quarter_value + dime_value + nickel_value + penny_value
    # print(round(total_cost, 2))

    return True if coffee_cost == round(total_cost, 2) else False

def run_again():
    user_choice = input('Do you want to order again "y" or "n": ?: ')
    return True if user_choice == 'y' else False

while run_coffee_machine:
    user_input = input(f'\nWhat would you like? : \t'
                       f'Espresso ${MENU["espresso"]["cost"]} \t'
                       f'Latte ${MENU["latte"]["cost"]} \t'
                       f'Cappuccino ${MENU["cappuccino"]["cost"]} \n').lower()

    if user_input == 'off':
        print('Shutting down....')
        run_coffee_machine = False

    elif user_input == 'report':
        report(resources)
        run_coffee_machine = run_again()

    elif user_input in MENU.keys():
        if check_resources(MENU[user_input]['ingredients']):
            print(f'Please insert coins: ${MENU[user_input]["cost"]}')
            quarter_coins = int(input('Insert quarters: '))
            dime_coins = int(input('Insert dimes: '))
            nickel_coins = int(input('Insert nickels: '))
            penny_coins = int(input('Insert pennies: '))

            if coin_calculator(quarter=quarter_coins,
                               dime=dime_coins,
                               nickel=nickel_coins,
                               penny=penny_coins,
                               coffee=user_input):
                prepare_coffee(MENU[user_input])
                report(resources)
                run_coffee_machine = run_again()
            else:
                print("Wrong number of coins added. Money refunded")
                run_coffee_machine = run_again()

        else:
            run_coffee_machine = run_again()
    else:
        print("Sorry, Not available")
        run_coffee_machine = run_again()

