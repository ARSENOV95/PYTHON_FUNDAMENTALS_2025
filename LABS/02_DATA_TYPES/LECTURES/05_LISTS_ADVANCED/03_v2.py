unsorted = [] #list to hold unsorted items

while True: #while End is entered, append commands to the list
    command = input()

    if command ==  "End":
        break

    unsorted.append(command)

sorted_list = sorted(unsorted,key = lambda x: x.split("-")[0]) #sort the jey by using the int part of the command 1-BLA as a key ( 1 ) index (0)
final = [char.split("-")[1] for char in sorted_list] #the final list will take the fist character of every 

print(final)