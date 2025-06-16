encoded_message = input().split(" ")


command = input()

while command != "3:1":
    
    full_command = command.split(" ")
    
    command_body = full_command[0]
    start_index = int(full_command[1])
    end_index = int(full_command[2])

    if command_body == 'merge':
        if end_index > len(encoded_message):
            end_index = -1

        merged = encoded_message[start_index:end_index]
        merged = ''.join(merged)
        
        del(encoded_message[start_index : end_index])
        encoded_message.insert(start_index,merged)

    #if command_body == 'devide':



    print(encoded_message)
    command = input()





