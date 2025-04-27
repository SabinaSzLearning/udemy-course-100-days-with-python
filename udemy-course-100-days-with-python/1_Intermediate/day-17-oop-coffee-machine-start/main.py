from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
maker = CoffeeMaker()
menu = Menu()

end = True
while end:
    userin = input(f"What would you like? ({(menu.get_items())}): ")
    if userin == "off":
        end = False
    elif userin == "report":
        maker.report()
    elif userin == "espresso" or userin == "latte" or userin == "cappuccino":
        item = menu.find_drink(userin)
        enough = maker.is_resource_sufficient(item)
        if enough:
            payOk = money.make_payment(item.cost)
            if payOk:
                maker.make_coffee(item)
        else:
            print("Not enough resources")