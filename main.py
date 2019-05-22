def coffee_machine_info(coffee_machine):
    print('The coffee machine has:')
    for key, value in coffee_machine.items():
        print(f'{value} of {key}')

    print()


def buy_coffee(coffee_machine, water=0, milk=0, beans=0, disposable_cups=0, money=0):
    if coffee_machine['water'] - water < 0:
        return 'Sorry, not enough water!'
    elif coffee_machine['milk'] - milk < 0:
        return 'Sorry, not enough milk!'
    elif coffee_machine['beans'] - beans < 0:
        return 'Sorry, not enough beans!'
    elif coffee_machine['disposable_cups'] - disposable_cups < 0:
        return 'Sorry, not enough disposable cups!'
    else:
        coffee_machine['water'] -= water
        coffee_machine['milk'] -= milk
        coffee_machine['beans'] -= beans
        coffee_machine['disposable_cups'] -= disposable_cups
        coffee_machine['money'] += money
        return 'I have enough resources, making you a coffee!'


def fill_coffee_machine(coffee_machine, water=0, milk=0, beans=0, disposable_cups=0):
    coffee_machine['water'] += water
    coffee_machine['milk'] += milk
    coffee_machine['beans'] += beans
    coffee_machine['disposable_cups'] += disposable_cups


def take_money(coffee_machine):
    money = coffee_machine['money']
    coffee_machine['money'] = 0
    return money


coffee_machine = {}
coffee_machine['water'] = 400
coffee_machine['milk'] = 540
coffee_machine['beans'] = 120
coffee_machine['disposable_cups'] = 9
coffee_machine['money'] = 550

action = input('Write action (buy, fill, take, remaining, exit): ')

while action != 'exit':
    if action == 'buy':
        coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        print()
        if coffee_type == '1':
            print(buy_coffee(coffee_machine, water=250, beans=16, disposable_cups=1, money=4))
        elif coffee_type == '2':
            print(buy_coffee(coffee_machine, water=350, milk=75, beans=20, disposable_cups=1, money=7))
        elif coffee_type == '3':
            print(buy_coffee(coffee_machine, water=200, milk=100, beans=12, disposable_cups=1, money=6))
        elif action == 'back':
            continue
    elif action == 'fill':
        water = int(input('Write how many ml of water do you want to add: '))
        milk = int(input('Write how many ml of milk do you want to add: '))
        beans = int(input('Write how many grams of coffee beans do you want to add: '))
        disposable_cups = int(input('Write how many disposable cups of coffee do you want to add: '))
        
        fill_coffee_machine(coffee_machine, water, milk, beans, disposable_cups)
        print()
        coffee_machine_info(coffee_machine)
    elif action == 'take':
        money = take_money(coffee_machine)
        print(f'I gave you ${money}\n')
    elif action == 'remaining':
        coffee_machine_info(coffee_machine)
    
    action = input('Write action (buy, fill, take, remaining, exit): ')
