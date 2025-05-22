import sys

number_of_snowballs = int(input())

highest_value = -sys.maxsize 
result = '' #variable to store the final result

for snawballs in range (number_of_snowballs):
    snowball_weight = int(input())        
    target_time = int(input())
    snowball_quality  = int(input())

    snowball_value = 0

    snowball_value = (snowball_weight/target_time) **snowball_quality
    if snowball_value > highest_value:   #if the value of the snallball is > the current largest value, it will become the new largest value 
        highest_value = snowball_value

        #calculations for the final result based on the largest value 
        result= f"{snowball_weight} : {target_time} = {int(snowball_value)} ({snowball_quality})" 

print(result)