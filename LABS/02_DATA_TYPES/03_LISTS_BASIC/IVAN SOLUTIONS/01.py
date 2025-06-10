numbers_as_string = input().split(" ")

number_as_integers = []

for current_number in numbers_as_string:
    current_number_as_integer = -int(current_number)
    number_as_integers.append(current_number_as_integer)

print(number_as_integers)

