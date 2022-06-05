from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    m = Menu()
    coffee_machine = CoffeeMaker()
    select_options = m.get_items()
    coin_processor = MoneyMachine()
    running = True
    while running == True:
        option = input(f"What would you like? ({select_options}): ")
        if option == "report":
            coffee_machine.report()
            coin_processor.report()
        elif option == "off":
            running = False
        else:
            drink = m.find_drink(option)
            if drink:
                if coffee_machine.is_resource_sufficient(drink):
                    if coin_processor.make_payment(drink.cost):
                        coffee_machine.make_coffee(drink)


main()
