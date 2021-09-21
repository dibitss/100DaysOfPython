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
}

def report(resources, money):
    return f'''
    Water: {resources.get('water')}
    Milk: {resources.get('milk')}
    Coffee: {resources.get('coffee')}
    Money: ${money}
    '''

def enough_resources(selection, resources):
    ingredients = MENU[selection]["ingredients"]
    for resource in ingredients:
        if resources[resource] < ingredients[resource]:
            print(f'Sorry, there\'s not enough {resource}.')
            return False
    
    return True

def check_money(coins, selection):
    total = coins['quarters'] * .25
    total += coins['dimes'] * .1
    total += coins['nickels'] * .05
    total += coins['pennies'] * .01

    return round(total - MENU[selection]['cost'], 2)    

def update_resources(selection, resources):
    ingredients = MENU[selection]["ingredients"]
    for resource in ingredients:
        resources[resource] -= ingredients[resource]
    
    return resources

money = 0
turn_off = False
while not turn_off:
    selection = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if selection == 'off':
        turn_off = True
    elif selection == 'report':
        print(report(resources, money))
    elif selection == 'espresso' or selection == 'latte' or selection == 'cappuccino':
        if enough_resources(selection, resources):
            coins = {}
            coins['quarters'] = int(input('How many quarters? '))
            coins['dimes'] = int(input('How many dimes? '))
            coins['nickels'] = int(input('How many nickels? '))
            coins['pennies'] = int(input('How many pennies? '))

            transaction = check_money(coins, selection)
            if transaction < 0:
                print('Sorry that\'s not enough money. Money refunded.')
            if transaction >= 0:
                money += MENU[selection]['cost']
                resources = update_resources(selection, resources)

                print(f'Here\'s ${transaction} in change.')
                print(f'Here\'s your {selection} ☕. Enjoy!')

    else:
        print('Invalid option. This incident will be reported.')