def num_chairs(num_rooms):
    needed = 0
    free_chairs = 0
    
    for room in range(1,num_rooms + 1):
        chairs_needed_per_room = 0
        
        current_room = input().split(" ")

        if len(current_room[0]) < int(current_room[1]): 
            chairs_needed_per_room += int(current_room[1]) - len(current_room[0])
            print(f"{chairs_needed_per_room} more chairs needed in room {room}")
        
        elif len(current_room[0]) > int(current_room[1]):
            free_chairs += len(current_room[0]) - int(current_room[1])

        needed += chairs_needed_per_room

    if free_chairs - needed > 0:
        return f"Game On, {free_chairs} free chairs left"

        
number_of_rooms = int(input())
print(num_chairs(number_of_rooms))

