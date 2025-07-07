while True:
    input_string = input()

    if input_string == "end":
        break

    reverse_string = input_string[::-1] #creates a  reversed string
    print(f"{input_string} = {reverse_string}")