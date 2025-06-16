number_of_rooms = int(input()) #input for initia; number fo rooms 

adittional_chairs_total = 0
free_chairs = 0
    
for room in range(1,number_of_rooms + 1): #for each room  check if there are free chairs
    additional_chairs = 0  #variable to store 
    current_room = input().split(" ")


#CASES TO CHECK if the number of chares i neach room are enough
    if len(current_room[0]) < int(current_room[1]):   #if the number of chairs in a room are smaller then the number fo people add the value to the addtiona lcharis needed variable 
        additional_chairs += int(current_room[1]) - len(current_room[0])
        print(f"{additional_chairs} more chairs needed in room {room}") # print the given repsonse and the value of the aditional charis variable needed 
        adittional_chairs_total += additional_chairs
        
    else:
        free_chairs += len(current_room[0]) - int(current_room[1]) #if the charis are nough add the addtional chairs left to the free chairs variable
        

if free_chairs - adittional_chairs_total >= 0: #if in the end the left charis from all rooms are larger then the needed ones print the text
    print(f"Game On, {free_chairs - adittional_chairs_total} free chairs left")

