number_of_rooms = int(input())

total_chairs_left = 0

for room in range(1,number_of_rooms + 1):
    chairs_left = 0

    room_occupancy = input().split(" ")
    num_seats = len(room_occupancy[0])
    num_people = int(room_occupancy[1])

    chairs_left = num_seats - num_people

    if chairs_left < 0:

        print(f"{abs(chairs_left)} more chairs needed in room {room}")

    total_chairs_left += chairs_left

if total_chairs_left >= 0:
    print(f"Game On, {total_chairs_left} free chairs left")



 