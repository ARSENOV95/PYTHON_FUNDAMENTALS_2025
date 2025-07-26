cities = {}

while (command := input()) != 'Sail':
    city,population,gold = command.split("||")
    population = int(population)
    gold = int(gold)


    if city not in cities.keys():
        cities[city] = {'population':population,'gold':gold}
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold


while (command:= input()) != 'End':
    parts = command.split("=>")
    action = parts[0]
    city = parts[1]

    match action:
        case 'Plunder':
            people,gold = map(int,parts[2:])
            cities[city]['population'] -= people
            cities[city]['gold'] -= gold

            print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
            if cities[city]['gold'] == 0 or cities[city]['population'] == 0:
                print(f"{city} has been wiped off the map!")
                del cities[city]

        case 'Prosper':
            gold = int(parts[2])
            if gold < 0:
                print("Gold added cannot be a negative number!")
                continue
            cities[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city,values in cities.items():
        print(f"{city} -> Population: {values['population']} citizens, Gold: {values['gold']} kg")
    
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")