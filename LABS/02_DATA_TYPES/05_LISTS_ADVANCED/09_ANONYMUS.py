encoded_message = input().split(" ")

command = input()

while command != "3:1":
    
    command_body,start_index,end_index = command.split(" ") 
 
    start_index = int(start_index)
    end_index = int(end_index)


    if command_body == 'merge' and start_index in range(len(encoded_message)):
        merged = ''.join(encoded_message[start_index:end_index])

        del(encoded_message[start_index : end_index])
        encoded_message.insert(start_index,merged)
        
    
    elif command_body == 'devide':
        devisable_index = encoded_message[start_index]

        for index in devisable_index:
     



    command = input()


    print(encoded_message)


