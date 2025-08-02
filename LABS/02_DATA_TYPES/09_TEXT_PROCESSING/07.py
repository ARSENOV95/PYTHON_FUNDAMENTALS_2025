explosive_string = input()

final_string = ''
strenght = 0 

for i in range(len(explosive_string)):
    if strenght > 0 and explosive_string[i] != '>':
        strenght -= 1
    
    elif explosive_string[i] == '>':
        final_string += '>'
        strenght += int(explosive_string[i+1])
    else:
        final_string += explosive_string[i]

print(final_string)


    
    