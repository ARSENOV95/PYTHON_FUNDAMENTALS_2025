def valid_range (val :int)-> bool:
    return val in range(len(target_sequence))


    

target_sequence = [int(num) for num in input().split()] #we convert each element of the given input to an integer

while True:  
    index = input() #while true we enter a command

    if index == "End": #if the command is End we break the loop
        break
    target_index = int(index) #if the command is not End we convert it to an integer

    if not valid_range(target_index): #if the index is not valid we continue to the next iteration
        continue

    if  target_sequence[target_index] == -1: #check if the target is already shot
        continue
    
    shot_target = target_sequence[target_index]  #if not shot we store the value in a variable
    target_sequence[target_index] = -1 #the target will obatin  -1 as  value

    for target in range(len(target_sequence)): #we iterate trough the list of targets and check if the target is not already shot
        if target_sequence[target] == -1:
            continue
        #if the target is not shot we increase or decreas depending on the value
        if target_sequence[target] > shot_target:
            target_sequence[target] -= shot_target
        elif target_sequence[target] <= shot_target:
            target_sequence[target] += shot_target

    

print(f'Shot targets: {target_sequence.count(-1)} -> {" ".join([str(el) for el in target_sequence])}')


