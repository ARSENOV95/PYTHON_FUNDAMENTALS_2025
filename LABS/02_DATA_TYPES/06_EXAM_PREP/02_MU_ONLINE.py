MAX_HEALTH = 100

health = MAX_HEALTH
intial_coins = 0

dungeon_rooms = input().split("|")

for i in range(len(dungeon_rooms)):
    command,number = dungeon_rooms[i].split()

    number = int(number)

    if command == "potion":
        healed = min(number,MAX_HEALTH - health)
        # replaces the if by taking the min value from the tot health - curre health
        #if the number is bigger it meanas the current health + number <= 10
        #else we only heal to the max health amouth
        
        health += healed
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")


    elif command == "chest":
        intial_coins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number #i nall other cases we lose health to mosnters 

        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i + 1}") #as we take the current room (index + 1)
            break

else:   #if the loop is not broken it will enter the else block
    print("You've made it!")
    print(f"Bitcoins: {intial_coins}")
    print(f"Health: {health}")
