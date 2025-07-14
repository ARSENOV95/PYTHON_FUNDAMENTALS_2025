def final_message(string :str)-> str:

    current_string = ''
    message = ''
    count_unique_chars = []
    num = ''

    for index in range(len(string)):
        if not(string[index].isdigit()):
            lower = string[index].lower()
            if lower not in count_unique_chars:
                count_unique_chars.append(lower)
            current_string += string[index]

        else:
            for next_char in range(index,len(string)):
                if not string[next_char].isdigit():
                    break
                num += string[next_char]
  
            message += (current_string * int(num)).upper()
            current_string = ''
            num= ''

    return f"Unique symbols used: {len(count_unique_chars)} \n{message}"

intial_string = input()

print(final_message(intial_string))
