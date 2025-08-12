def change(character :str,new_character,orig_string :str)->str:
    if character in orig_string:
        orig_string = orig_string.replace(character,new_character)
    print(orig_string)    
    return orig_string

def includes(substr :str,orig_string :str)->bool:
    result = substr in orig_string
    return print(result)

def end(substr :str,orig_string :str)->bool:
    result = orig_string.endswith(substr)
    return print(result)

def find_index(character :str,orig_string :str)->int:
    if character in orig_string:
        idx = orig_string.find(character)
        return print(idx)
    else:
        return print(orig_string)
    
def cut(start_idx :int,chars :int,string :str)->str:
    final_idx = start_idx + chars
    cut_string = string[start_idx:final_idx]
    return print(cut_string)

string = input()

while (command := input()) != "Done":
    command_parts = command.split()
    action = command_parts[0]

    if action == "Change":
        char,replacement = command_parts[1:]
        string = change(char,replacement,string)

    elif action == "Includes":
        substring = command_parts[1]
        includes(substring,string)

    elif action == "End":
        substring = command_parts[1]
        end(substring,string)
    
    elif action == "Uppercase":
        string = string.upper()
        print(string)

    elif action == "FindIndex":
        char = command_parts[1]
        find_index(char,string)
    
    else:
        start_index,num_chars  = map(int,(command_parts[1:]))
        cut(start_index,num_chars,string)
    
    