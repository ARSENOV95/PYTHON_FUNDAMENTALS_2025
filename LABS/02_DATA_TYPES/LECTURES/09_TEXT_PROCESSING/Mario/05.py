text = input()

numbers = ''
letters = ''
chars  = ''

for char in text:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        chars += char

print(f"{numbers}\n{letters}\n{chars}")