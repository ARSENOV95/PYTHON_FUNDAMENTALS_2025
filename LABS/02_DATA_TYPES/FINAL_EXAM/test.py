inbox_capacity = int(input())

inbox = {}

while (command := input()) != "Statistics":
    command_elements = command.split('=')
    action,user = command_elements[:2]
    #print(action,user)

    if action == "Add":
        sent,received = map(int,command_elements[2:])
        #print(sent,received)
        if user not in inbox.keys():
            inbox[user]  = {'sent':0,'received':0}
        inbox[user]  = {'sent':sent,'received':received}

    elif action == 'Message':
        sender = user
        receiver = command_elements[2]
        #print(sender,receiver,'sender receiver')

        if sender in inbox.keys() and receiver in inbox.keys():
            inbox[sender]['sent'] += 1
            #print(inbox[sender]['sent'],'sent message count')

            if inbox[sender]['sent'] + inbox[sender]['received'] >= inbox_capacity:
                print(f"{sender} reached the capacity!")
                del inbox[sender]
                #print(inbox,'check after sender deletion')

            inbox[receiver]['received'] += 1
            #print(inbox[receiver]['received'],'received messages')

            if inbox[receiver]['sent'] + inbox[receiver]['received'] >= inbox_capacity:
                print(f"{receiver} reached the capacity!")
                del inbox[receiver]


    elif action == 'Empty':
        #print(user)
        if user == 'All':
            inbox.clear()
        elif user in inbox.keys():
            del inbox[user]

print(f'Users count: {len(inbox)}')

for users,messages in inbox.items():
    count = sum(messages.values())
    if count > 0:
        print(f"{users} - {count}")
