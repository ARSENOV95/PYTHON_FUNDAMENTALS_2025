initial_string = input()

while (command := input()) != "Decode":
    action = command.split("|")
    do = action[0]

    if do == "Move":
        number_of_letters = int(action[1])
        initial_string = initial_string[number_of_letters:] + initial_string[:number_of_letters]

    elif do == "Insert":
        index = int(action[1])
        value = action[2]
        initial_string =  initial_string[:index] + value + initial_string[index:]
    
    elif do == "ChangeAll":
        substring = action[1]
        replacement = action[2]
        initial_string = initial_string.replace(substring,replacement)

print(f"The decrypted message is: {initial_string}")