initial_energy  = int(input())
current_energy = initial_energy
won_battles = 0

while True:
    if won_battles %3 == 0:
        current_energy += won_battles

    command = input()

    if command == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {current_energy}")
        break

    distance = int(command)

    if distance <= 0:
        continue

    if current_energy - distance >= 0:
        won_battles += 1
        current_energy -= distance

    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {current_energy} energy")
        break




