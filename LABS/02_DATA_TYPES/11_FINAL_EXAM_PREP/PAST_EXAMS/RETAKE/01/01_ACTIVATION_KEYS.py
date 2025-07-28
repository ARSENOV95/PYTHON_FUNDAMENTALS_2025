def check_substring (substr :str,key :str)->str:
    if substr in key:
        return f"{key} contains {substr}"
    return "Substring not found!"
    
def upper_lower (start :int,end :int,act :str,key :str)->str:
    if start in range(len(key)) and end in range(len(key)):
        modified = '' 
        if act == 'Upper':
            modified = key[start:end].upper()
        elif act == 'Lower':
            modified = key[start:end].lower()

        key = key[:start] + modified + key[end:]
        return  key


def slicer (start :int,end :int,key :str)->str:
    key = key[:start] + key [end:]
    return key

raw_key = input()

while (command := input()) != 'Generate':
    parts = command.split('>>>')
    action = parts[0]

    match action:
        case 'Contains':
            substring = parts[1]
            print(check_substring(substring,raw_key))

        case 'Flip':
            upper_or_lower = parts[1]
            start_index,end_index = map(int,parts[2:])
            raw_key  = (upper_lower(start_index,end_index,upper_or_lower,raw_key))
            print(raw_key)

        case 'Slice':
            start_index,end_index = map(int,parts[1:])
            raw_key = (slicer(start_index,end_index,raw_key))
            print(raw_key)

print(f"Your activation key is: {raw_key}")