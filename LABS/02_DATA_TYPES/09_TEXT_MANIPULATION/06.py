string = input()

prev_char = ''
final = ''

for char in string:
    if char != prev_char:
        final += char

    prev_char = char 

print(final)

