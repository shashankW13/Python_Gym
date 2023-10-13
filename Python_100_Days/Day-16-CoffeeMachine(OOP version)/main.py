from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

run_coffee_machine = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
def run_again():
    user_choice = input('\nDo you want to order again "y" or "n": ?: ')
    return True if user_choice == 'y' else False

while run_coffee_machine:
    user_input = input(f'\nWhat would you like? : {menu.get_items()} \n').lower()

    if user_input == 'off':
        print('Shutting down....')
        run_coffee_machine = False

    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
        run_coffee_machine = run_again()

    elif menu.find_drink(user_input) is not None:
        coffee = menu.find_drink(user_input)
        coffee_cost = menu.find_drink(user_input).cost
        if coffee_maker.is_resource_sufficient(coffee):
            print(f'Cost: ${coffee_cost}')
            if money_machine.make_payment(coffee_cost):
                coffee_maker.make_coffee(coffee)
                run_coffee_machine = run_again()
            else:
                run_coffee_machine = run_again()
        else:
            run_coffee_machine = run_again()

    else:
        run_coffee_machine = run_again()