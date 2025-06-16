number_sequence = list(map(int,input().split(","))) 


group = 0 #inital value of the group wich we will increase on every itteration 

while len(number_sequence) > 0: #while the original list is > 0

    #1 -- we will increase the group by 10
    group += 10
    
    #2 == we will iterate trough every element in the list and append to a new list only those elements with value <= group var (10,20,30,40)
    grouped_result = [number  for number in number_sequence if number <= group]
    
    #3 we prepare the initial list by assging every element not found in the current grouped list 
    number_sequence = list(filter(lambda x: x not in grouped_result,number_sequence))

    print(f"Group of {group}'s: {grouped_result}")

    

    


