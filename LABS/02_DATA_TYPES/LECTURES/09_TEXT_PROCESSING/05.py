input_string = input()

numbers = letters = special = ''

for char in input_string:
    if char.isnumeric():
        numbers += char
    elif char.isalpha():
        letters += char       
    else:
        special += char

print(numbers)
print(letters)
print(special)


