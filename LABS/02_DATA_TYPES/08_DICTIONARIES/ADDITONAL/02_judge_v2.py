users = {}

#users = {'pesho':{'C#':100,'JAVA':50},
#         'Gosho':{'Python':10,'C++':87}
#\         }

command = input()

while True:

    if command == 'no more time':
        break
  
    command_components = command.split(" -> ")
    username,contest,points = command_components[0],command_components[1],int(command_components[2])

    if not(points in range(0,1001)):
        continue

    if username not in users.keys():
        users[username] = {contest:points}
    else:
        if contest in users[username].keys() and users[username][contest] < points:
            users[username][contest] = points
        else:
            users[username][contest] = points

    command = input()

#print(users)

