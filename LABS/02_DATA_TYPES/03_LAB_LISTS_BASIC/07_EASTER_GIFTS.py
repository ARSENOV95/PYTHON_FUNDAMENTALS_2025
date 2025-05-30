
list_of_gifts = list(map(str,input().split( )))

command = input()
list_command = list(map(str,command.split()))


while command != "No Money":
    if list_command[0] == 'OutOfStock':
        for gift in list_of_gifts:
            if gift == list_command[1]:
                list_of_gifts.remove(gift)

    elif list_command[0] == 'Required':
        for gift_index in range(len(list_of_gifts)):
            if  list_command[2] ==  gift_index:
                list_of_gifts[gift_index] = list_command[1]
    
    elif list_command[0] == 'JustInCase':
         list_of_gifts[-1] == list_command[1]

    

    command = input()

print(list_of_gifts)