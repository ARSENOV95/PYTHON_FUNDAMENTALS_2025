def validate_action(act: str)->bool:
    if act == 'Drive' or 'Refuel' or 'Revert':
        return True
    else:
        return False

def validate_vehicle(vehicle :str,dc :dict)->bool:
    return vehicle in dc.keys()

number_of_cars = int(input())
cars = {}

max_fuel = 75

for i in range(number_of_cars):
    car_info = input().split('|')
    car,milage,fuel = car_info
    milage = int(milage)
    fuel = int(fuel)

    if car not in cars:
        cars[car] = {}
    cars[car] = [milage,fuel]

while (command:= input()) != 'Stop':
    actions = command.split(" : ")
    action = actions[0]
    make = actions[1]

    if not validate_action(action):
        continue

    if not validate_vehicle(make,cars):
        continue

    if action == 'Drive':
        miles,fuel = actions[2:]
        miles = int(miles)
        fuel = int(fuel)

        if cars[make][1] >= fuel:
           cars[make][0] += miles
           cars[make][1] -= fuel
           print(f"{make} driven for {miles} kilometers. {fuel} liters of fuel consumed.")
        else:
            print('Not enough fuel to make that ride')

    elif action == 'Refuel':
        fuel = actions[2]
        fuel = int(fuel)
        fuel_needed = min(max_fuel - cars[make][1],fuel)
        cars[make][1] += fuel_needed
        print(f"{make} refueled with {fuel_needed} liters")
    elif action == 'Revert':
        miles = actions[2]
        miles= int(miles)
        if cars[make][0] > miles and cars[make][0] -miles >= 10000:
            cars[make][0] -= miles
            print(f"{make} mileage decreased by {miles} kilometers")
        elif cars[make][0] -miles >= 10000:
            cars[make][0] = 10000

for car,info in cars.items():
    print(f"{car} -> Mileage: {info[0]} kms, Fuel in the tank: {info[1]} lt.")