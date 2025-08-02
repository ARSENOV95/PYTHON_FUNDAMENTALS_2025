intial_energy  = 100
inital_coins = 100

current_energy = intial_energy
current_coins = inital_coins

info = input().split('|')

closed = False

for curent_info in info:
    current_event = curent_info.split('-')

    event,quantity = current_event[0],int(current_event[1])

    if event == 'rest':
        gained_energy = min(intial_energy - current_energy,quantity)
        current_energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")
        
    elif event == 'order':
        if current_energy >= 30:
            current_energy -= 30
            current_coins += quantity
            print(f"You earned {quantity} coins.")
        else:
            current_energy += 50
            print("You had to rest!")
    else:
        if current_coins >= quantity:
            current_coins -= quantity
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            closed = True
            break 
        
if not closed:
    print('Day completed!')
    print(f'Coins: {current_coins}\nEnergy: {current_energy}')
