list_of_gifts = input().split() #list of items recieved on a single line with " " as a separator (all strings)

command = input()

key_word = "No Money"

while command != key_word:
    current_command = command.split()
    
    command_text = current_command[0]
    command_item = current_command[1]

    if len(current_command) > 2:
        command_replace_index = int(current_command[2])
    
    if command_text == 'OutOfStock':
        for gift in range(len(list_of_gifts)):
            if list_of_gifts[gift] == command_item:
                list_of_gifts[gift] = "None"

        
    elif command_text == 'Required' and (0 <= command_replace_index < len(list_of_gifts)):
        list_of_gifts[command_replace_index] = command_item
            
    elif command_text == 'JustInCase':
        list_of_gifts[-1] = command_item

    command = input()

while "None" in list_of_gifts:
    list_of_gifts.remove("None")

final_result = " ".join(list_of_gifts)

print(final_result)