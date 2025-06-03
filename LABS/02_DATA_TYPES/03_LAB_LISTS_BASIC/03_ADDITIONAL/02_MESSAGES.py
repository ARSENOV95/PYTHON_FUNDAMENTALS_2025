sequence_of_numbers = input().split(" ")
lookup_string = input()

list_of_chars = []

for index in lookup_string:
    list_of_chars.append(index)


final_message = []

for numbers in sequence_of_numbers:
    number_set = [int(num) for num in numbers]
    lookup_number = sum(number_set)


    if lookup_number in range(len(list_of_chars)):
        char = list_of_chars.pop(lookup_number)
        
    else:
        char = list_of_chars.pop(lookup_number - len(list_of_chars))

    final_message.append(char)

print("".join(final_message))
