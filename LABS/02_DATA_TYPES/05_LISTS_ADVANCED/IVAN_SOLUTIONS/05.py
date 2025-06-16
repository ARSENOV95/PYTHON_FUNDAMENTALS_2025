number_of_rooms = int(input())

total_chairs = 0

for number_of_room in range(len(number_of_rooms + 1)):
    chairs_in_current_room,visitors = input().split()
    diff = len(chairs_in_current_room) - int(visitors)

    if diff < 0:
        print(f"{abs(diff)} more chairs needed in room {number_of_room}")

    total_chairs += diff

if total_chairs >= 0:
    print(f"Game On, {total_chairs} free chairs left")