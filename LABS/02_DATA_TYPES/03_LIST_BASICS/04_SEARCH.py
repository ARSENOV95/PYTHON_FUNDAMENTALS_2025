number_of_strings = int(input())

seatch_criteria = input()

list_of_strings = [] 
filtered_list = []


for current_string in range(number_of_strings):
    new_string = input()

    list_of_strings.append(new_string)

    if seatch_criteria in new_string:
        filtered_list.append(new_string)


print(f"{list_of_strings} \n{filtered_list}")

