while True:
    input_string = input()

    if input_string == "end":
        break
    
    reverse_string = ''
    for char in range(len(input_string),-1,-1):
        reverse_string += input_string[char] #a loop trough go trough the string in reverse  and save it into a new string 

    print(f"{input_string} = {reverse_string}")