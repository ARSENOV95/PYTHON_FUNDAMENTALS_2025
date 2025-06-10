sequence_of_numbers = input().split(" ") #a list with a set of numbers needed to find the index
lookup_string = input() # string from which we have to 

list_of_chars = [] #an emtyp string used to convert  the lookup string into a list character by character

for index in lookup_string: #a loop to append every element of the string into the lookup list
    list_of_chars.append(index)


final_message = [] #a final string to store the elements st

for numbers in sequence_of_numbers:
    number_set = [int(num) for num in numbers]
    lookup_number = sum(number_set)


    if lookup_number in range(len(list_of_chars)):
        char = list_of_chars.pop(lookup_number)
        
    else:
        char = list_of_chars.pop(lookup_number - len(list_of_chars))

    final_message.append(char)

print("".join(final_message))
