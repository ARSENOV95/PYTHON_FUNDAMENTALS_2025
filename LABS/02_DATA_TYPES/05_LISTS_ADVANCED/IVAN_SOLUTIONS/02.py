version = [int(digit) for digit in input().split(".")]
#takes every symbol form the initally split list and coverts to int 

version[-1] += 1 #intially we set the version to be 1 number hight (the last digit)

for index in range(len(version)-1,0,-1): #for every itteration we check the digits, if the current digit is >9, then we set it to 0 and inceres the oone beforehand 
    if version[index] > 9:
        version[index] = 0
        version[index -1] += 1 


print(".".join(str(digit) for digit in [version]))
