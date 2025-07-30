def odds (pswd :str)->str:
    new_paswd = pswd[1::2]
    print(new_paswd)
    return new_paswd

def cut(idx :int,len_ :int,pswd :str)->str:
    end_idx = (idx + len_)

    pswd = pswd[:idx] + pswd[end_idx:]
    print(pswd)
    return pswd

def substitute(old :str,new :str,pswd :str)->str:
    if old in pswd:
        pswd = pswd.replace(old,new)
        print(pswd)
    else:
        print("Nothing to replace!")
    return pswd
    

password = input()

while (command := input()) != 'Done':
    command_body = command.split()
    action = command_body[0]

    match action:
        case 'TakeOdd':
            password = odds(password)
            
        case 'Cut':
            index,lenght = map(int,command_body[1:])
            
            password = cut(index,lenght,password)
        case 'Substitute':
            old_susbstring, new_substring = command_body[1:] 
            password = substitute(old_susbstring,new_substring,password)
    
    
print(f"Your password is: {password}")
