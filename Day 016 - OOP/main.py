from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

off = False
while not off:
    selection = input(f'What would you like? ({menu.get_items()}): ')
    if selection == 'off':
        off = True
    elif selection == 'report':
        coffee_maker.report()
        money_machine.report()
    elif selection in menu.get_items():
        drink = menu.find_drink(selection)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else: 
        print('Invalid option. This incident will be reported.')