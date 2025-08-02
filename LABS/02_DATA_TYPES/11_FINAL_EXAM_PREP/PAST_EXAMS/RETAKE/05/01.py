#function 1 #change all letters to upper/lower
def letters(arg :str,usr :str)->str:
    match arg:
        case 'Lower':
            usr = usr.lower()
        case 'Upper':
            usr = usr.upper()
    print(usr)
    return usr

#function 2 revers a substring with valid indexes
def reverse(s_idx :int,e_idx :int,usr :str):
    if s_idx in range(len(usr)) and e_idx in range(len(usr)) and s_idx >= 0 and e_idx >= 0:
        sub = usr[s_idx:e_idx + 1] #both indexes are inclusive
        print(sub[::-1])


def substr(sub :str,usr :str)->str:
    if sub in usr:
        start_idx = usr.find(sub)
        end_idx = start_idx + len(sub)
        usr = usr[:start_idx] + usr[end_idx:]
        print(usr)
    else:
        print(f"The username {usr} doesn't contain {sub}.")
    return usr

def replace(char :str,usr :str)->str:
    if char in usr:
        usr = usr.replace(char,'-')
        print(usr)
    return usr

def validation(char :str,usr :str):
    if char in usr:
        return print("Valid username.")
    else:
        return print(f"{char} must be contained in your username." )


username  = input()

while (command := input()) != "Registration":
    command_parts = command.split()
    action = command_parts[0]

    match action:
        case "Letters":
            argument = command_parts[1]
            username = letters(argument,username)

        case "Reverse":
            start,end = map(int,command_parts[1:])
            reverse(start,end,username) #only prints a reveres substring

        case "Substring":
            substring = command_parts[1]
            username = substr(substring,username)

        case "Replace":
            character = command_parts[1]
            username = replace(character,username)

        case "IsValid":
            character = command_parts[1]
            validation(character,username)