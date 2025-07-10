input_string = input().split(" ")
emoji = []

for string in input_string:
    if string.startswith(":"):
        emoji.append(string[:2]) #takes 1 symbol after the :

print('\n'.join(emoji))