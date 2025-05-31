a_list_of_numbers = input().split(", ")

a_list_of_numbers = [int(integer) for integer in a_list_of_numbers]

final_list = []

zero_count = a_list_of_numbers.count(0)


for number in a_list_of_numbers:
    if number != 0:
        final_list.append(number)


final_list.extend([0] * zero_count)
print(final_list)

