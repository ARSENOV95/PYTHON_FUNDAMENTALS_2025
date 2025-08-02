list_of_usernames = input().split(", ") #input string with passwords 
valid_names = []  #enopty string to store valid passpwrds

redundent = ("_","__","-","--") # a tuple of redundent symbols

for username in list_of_usernames:
    if not (3 <= len(username) <= 16): #check 1 if the lenght of the pass word is  3 or more and less or equal to 16
        continue
    
    if not (username.isalnum() or"-" in username or "_" in username): #check 2 if the username consists of nmbers.letters -  or _
        continue
    
    if len(username) %2 == 0:             #check 3 part 1 - if even lenght check if the middle two symbols are redundent
        mid_lef = len(username)/2 - 1
        mid_right= len(username)/2
        if mid_lef == mid_right:
            continue
    
    if not (username[0].startswith(redundent) or username[0].endswith(redundent)): #check 3 if the user starts/ends with any of the redundnet symbols
        valid_names.append(username)
       
print('\n'.join(valid_names))


        