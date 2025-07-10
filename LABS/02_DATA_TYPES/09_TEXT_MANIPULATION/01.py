list_of_usernames = input().split(", ")
valid_names = []

redundent = ("_","__","-","--")

for username in list_of_usernames:
    if not (3 <= len(username) <= 16):
        continue
    
    if not (username.isalnum() or"-" in username or "_" in username):
        continue
    
    if len(username) %2 == 0:
        mid_lef = len(username)/2 - 1
        mid_right= len(username)/2
        if mid_lef == mid_right:
            continue
    
    if not (username[0].startswith(redundent) or username[0].endswith(redundent)):
        valid_names.append(username)
       
print('\n'.join(valid_names))


        