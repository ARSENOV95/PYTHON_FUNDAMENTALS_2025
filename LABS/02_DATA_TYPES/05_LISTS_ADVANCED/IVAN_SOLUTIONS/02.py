version = [int(digit) for digit in input().split(".")]
#takes every symbol form the initally split list and coverts to int 

version[-1] += 1 

for index in range(len(version)-1,0,-1):
    if version[index] > 9:
        version[index] = 0
        version[index -1] += 1 

