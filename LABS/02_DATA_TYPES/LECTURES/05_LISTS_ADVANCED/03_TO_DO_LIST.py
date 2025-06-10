notes = [0] * 10

command_input = input()


while command_input != "End":
    command_body = command_input.split("-") #a slit to hwo the different pats of a command - priority and taks
    
    priority = int(command_body[0]) - 1 #the priority is given, but to be on the opt of the list we can use it as an index, 
    #then we need to subtract 1 from the value, the priority 1 on the task will have value 0 and be appended as a first eleement

    task = str(command_body[1])

    notes.pop(priority) # removes value from index 0
    notes.insert(priority,task)

    command_input = input()


while 0 in notes:
    notes.remove(0)

print(notes)






