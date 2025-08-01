number_of_heroes = int(input())

heroes_vitals = {}


for hero in range(number_of_heroes):
    hero_data = input().split()
    name = hero_data[0]
    hp,mp = map(int,hero_data[1:])

    if hp > 100 or mp > 200:
        continue

    if name not in heroes_vitals.keys():
        heroes_vitals[name] = {'HP':hp, 'MP':mp}
    else:
        if  heroes_vitals[name]['HP'] + hp <= 100 and heroes_vitals[name]['MP'] + mp <= 200:
            heroes_vitals[name]['HP'] += hp
            heroes_vitals[name]['MP'] += mp
    


while (command := input()) != 'End':
    command_body = command.split(' - ')
    action,name = command_body[:2]

    match action:
        case 'CastSpell':
            needed_mp,spell = command_body[2:]
            needed_mp = int(needed_mp)
            if heroes_vitals[name]['MP'] >= needed_mp:
                heroes_vitals[name]['MP'] -= needed_mp
                print(f"{name} has successfully cast {spell} and now has {heroes_vitals[name]['MP']} MP!")
            else:
                print(f"{name} does not have enough MP to cast {spell}!")
        
        case 'TakeDamage':
             damage,attacker = int(command_body[2]),command_body[3]
             if damage < heroes_vitals[name]['HP']:
                 heroes_vitals[name]['HP'] -= damage
                 print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_vitals[name]['HP']} HP left!")
             elif damage >= heroes_vitals[name]['HP']:
                 del heroes_vitals[name]
                 print(f"{name} has been killed by {attacker}!")
        
        case 'Recharge':
            amount = int(command_body[2])
            mana_needed = min((200 - heroes_vitals[name]['MP']),amount)
            
            heroes_vitals[name]['MP'] += mana_needed
            print(f"{name} recharged for {mana_needed} MP!")

        case 'Heal':
            amount = int(command_body[2])
            health_needed = min((100 - heroes_vitals[name]['HP']),amount)
            
            heroes_vitals[name]['HP'] += health_needed
            print(f"{name} healed for {health_needed} HP!")


for name,vitals in heroes_vitals.items():
    print(name)
    print(f" HP: {vitals['HP']}")
    print(f" MP: {vitals['MP']}")