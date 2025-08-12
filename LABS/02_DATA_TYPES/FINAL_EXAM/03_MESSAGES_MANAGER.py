inbox_capacity = int(input())

inbox = {}

while (command := input()) != 'Statistics':
    command_elements = command.split('=')
    action,user = command_elements[:2]

    match action:
        case 'Add':
            sent,received = map(int,command_elements[2:])
            if user not in inbox.keys():
                inbox[user]  = {'sent':0,'received':0}
            inbox[user]  = {'sent':sent,'received':received}
  
        case 'Message':
            sender = user
            receiver = command_elements[2]

            if sender in inbox.keys() and receiver in inbox.keys():
               inbox[sender]['sent'] += 1
               inbox[receiver]['received'] += 1

               sender_inbox = sum(inbox[sender].values())
               receiver_inbox = sum(inbox[receiver].values())

               if sender_inbox >= inbox_capacity:
                  print(f"{sender} reached the capacity!")
                  del inbox[sender]

               if receiver_inbox >= inbox_capacity:
                  print(f"{receiver} reached the capacity!")
                  del inbox[receiver]

        case 'Empty':
            if user == 'All':
               inbox.clear()

            elif user in inbox.keys():
                del inbox[user]


print(f"Users count: {len(inbox)}")

for user,messages in inbox.items():
    message_count = sum(messages.values())
    print(f"{user} - {message_count}")
