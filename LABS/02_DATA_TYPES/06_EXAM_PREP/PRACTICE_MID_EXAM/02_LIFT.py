total_num_people = int(input())
total_wagon_capacity = 4

lift_state = input().split()


for wagon_number in range(len(lift_state)):
    current_load = min(total_num_people,(total_wagon_capacity - int(lift_state[wagon_number])))
    total_num_people -= current_load
    lift_state[wagon_number] = int(lift_state[wagon_number]) + current_load

wagon_capacity = [str(wagon) for wagon in lift_state]

if total_num_people > 0 and sum(lift_state) == len(lift_state) * total_wagon_capacity:
   print(f"There isn't enough space! {total_num_people} people in a queue!")
elif total_num_people == 0 and sum(lift_state) < len(lift_state) * total_wagon_capacity:
    print("The lift has empty spots!")

print(f'{" ".join(wagon_capacity)}')

