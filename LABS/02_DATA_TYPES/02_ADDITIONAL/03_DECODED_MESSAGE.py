decription_key = int(input())
number_of_lines = int(input())

decripted_message = ""

for current_line in range(number_of_lines):
    letter = input()

    if letter.isalpha():
            decripted_message += chr(ord(letter) + decription_key)

    else:
        print("Not a valid letter!")
        break

print(decripted_message)