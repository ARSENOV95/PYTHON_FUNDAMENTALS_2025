energy = 100

battles_won = 0

while True:
    command = input()

    if command == "End of battle ":
        print(f"Won battles: {battles_won}. Energy left: {energy}")
        break

    if command.isnumeric():
        enemy_distance = int(command)

    if energy - enemy_distance >= 0:
        energy -= enemy_distance
        battles_won += 1
    
    if battles_won %3 == 0:
        energy += battles_won

    else:
        energy == 0
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")