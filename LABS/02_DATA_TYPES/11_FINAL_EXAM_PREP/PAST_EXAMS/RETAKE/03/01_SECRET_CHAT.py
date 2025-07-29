def insert_space(idx :int,string :str)->str:
    if idx in range(len(string)):
        string = string[:idx] + ' ' + string[idx:]
        print(string)
    return string

def rev(substr :str,string :str)->str:
    if substr in string:
        start_idx = string.find(substr)
        end_idx = start_idx + len(substr) -1
        
        new_substr = string[start_idx:end_idx]
        string = string[:start_idx] + string[end_idx:]
        string += new_substr[::-1]
        print(string)
    else:
        print("error")

    return string

def change_all(substr :str,new_substr :str,string :str)->str:
    string = string.replace(substr,new_substr)
    print(string)
    return string

concealed_message = input()

while (command :=input()) != 'Reveal':
    command = command.split(':|:')
    action = command[0]

    match action:
        case 'InsertSpace':
            index = int(command[1])
            concealed_message = insert_space(index,concealed_message)
        case 'Reverse':
            substring = command[1]
            concealed_message = rev(substring,concealed_message)
        case 'ChangeAll':
            substring = command[1]
            new_substring = command[2]
            concealed_message = change_all(substring,new_substring,concealed_message)

print(f"You have a new text message: {concealed_message}")