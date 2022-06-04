

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


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def calc_received(q, d, n, p):
    q_tot = q * 0.25
    d_tot = d * 0.10
    n_tot = n * 0.05
    p_tot = p * 0.01
    return q_tot + d_tot+n_tot+p_tot


def user_pay(selected):
    drink_data = MENU[selected]
    cost_of_drink = drink_data['cost']
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    received = calc_received(quarters, dimes, nickles, pennies)
    if received >= cost_of_drink:
        confirm_purchase(received, selected)
    else:
        print("Sorry that's not enough Money. Money refunded.")


def confirm_purchase(received, option):
    drink_data = MENU[option]
    change = round(received-drink_data['cost'], 2)
    resources['money'] = resources['money'] + drink_data['cost']
    print(f"Here is ${change} in change.")
    print(f"Here is your {option}, enjoy!")


def make_drink(selected, resources):
    drink_data = MENU[selected]
    current_resources = dict(resources)
    for item in drink_data['ingredients']:
        if resources[item] >= drink_data['ingredients'][item]:
            resources[item] -= drink_data['ingredients'][item]
        else:
            # remove any changes if made before noticing not enough ingredient
            resources = current_resources
            print(f"Sorry there is not enough {item}.")
            return
    return user_pay(selected)


def coffee_machine():
    resources['money'] = 0
    running = True
    while running:
        option = input('What would you like? (espresso/latte/cappuccino): ')
        if option == 'report':
            report()
        elif option == 'off':
            running = False
        else:
            make_drink(option, resources)


coffee_machine()
