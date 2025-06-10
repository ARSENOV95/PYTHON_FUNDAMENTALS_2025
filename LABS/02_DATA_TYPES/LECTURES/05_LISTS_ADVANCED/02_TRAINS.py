number_of_carts = int(input())

train = [0] * number_of_carts

for current_cart in range(number_of_carts):
    train.append(0)

command = input()

while command != "End":

    current_command = command.split(" ")
    action = str(current_command[0])

    if len(current_command) < 3:
        passangers_number = int(current_command[1])
    else:
        passenger_seat = int(current_command[1])
        passangers_number = int(current_command[2])

    if action == 'add':
        train[-1] += passangers_number

    elif action == 'insert':
        train[passenger_seat] += passangers_number
    elif action == 'leave':
        train[passenger_seat] -= passangers_number

    command = input()
print(train)