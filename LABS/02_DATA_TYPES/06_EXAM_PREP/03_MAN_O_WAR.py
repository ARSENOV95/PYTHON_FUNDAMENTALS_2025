pireate_ship  = [int(el) for el in input().split(">")]
warship = [int(el) for el in input().split(">")]

max_health = int(input())
repair_health_treshhold = max_health * 0.2

while True:
    command = input()

    if command == 'Retire':
        print(f"Pirate ship status: {sum(pireate_ship)}")
        print(f"Warship status: {sum(warship)}")
        break

    if command.startswith('Fire'):
        idx, damage = [int(el) for el in command.split()[1:]] #split the command andtkae very element from 1st to n - 1
        if idx not in range(len(warship)):
            continue

        warship[idx] -= damage
        if warship[idx] <= 0:
            print("You won! The enemy ship has sunken.")
            break

    elif command.startswith('Defend'):
        start_idx,end_idx,damage = [int(el) for el in command.split()[1:]] #split the command andtkae very element from 1st to n - 1
        if not((0 <= start_idx < len(pireate_ship) and 0 <= end_idx < len(pireate_ship))):
            continue

        for i in range(start_idx,end_idx + 1):
            pireate_ship[i] -= damage
            if pireate_ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit() #diectly exit the program
            
    elif command.startswith('Repair'):
        idx, health = [int(el) for el in command.split()[1:]]
        if idx not in range(len(warship)):
            continue

        pireate_ship[idx] += min(health,max_health - pireate_ship[idx]) #repair the ship to the max health or the given health
        
    elif command.startswith('Status'): 

        for_reapir = sum(1 for sec in pireate_ship if sec < repair_health_treshhold) #for each element adds directly 1 to for_repair 
        print(f"{for_reapir} sections need repair.")


  


   