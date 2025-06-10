
list_of_numbers = list(map(int,input().split()))

list_of_inverted_numbers = []

for number in list_of_numbers:
    if number == 0:
        list_of_inverted_numbers.append(0)
    else:
        list_of_inverted_numbers.append(number.__invert__())

print(list_of_inverted_numbers)