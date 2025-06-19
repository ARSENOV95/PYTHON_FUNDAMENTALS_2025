def valid_range(idx :int,seq :list):
    return idx in range(len(seq))

list_of_taregets = [int(val) for val in input().split()]

while (command := input()) != "End":
    action,index,arg = command.split(" ")

    index = int(index)
    arg = int(arg)

    if action == "Shoot":
        if not valid_range(index,list_of_taregets):
            continue

        if (list_of_taregets[index] - arg) > 0:
            list_of_taregets[index] = (list_of_taregets[index] - arg) 
            
        else: 
            list_of_taregets.pop(index)
     
    elif action == "Add":
        if not valid_range(index,list_of_taregets):
            print("Invalid placement!")
            continue
    
        list_of_taregets.insert(index,arg)

        pass 
    elif action == "Strike":

        if not (valid_range(index,list_of_taregets) and index - arg in range(len(list_of_taregets)) and index + arg in range(len(list_of_taregets))):
            print("Strike missed!")
            continue
        
        end_range = index + arg
        start_range = index -arg

        for element in range(end_range,start_range -1,-1):
            list_of_taregets.pop(element)


print("|".join([str(el) for el in list_of_taregets]))

  



