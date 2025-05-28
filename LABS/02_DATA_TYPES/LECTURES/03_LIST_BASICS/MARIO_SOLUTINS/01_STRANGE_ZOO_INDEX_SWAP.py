my_list = []

for body_part in range(3):
    data = input()
    my_list.append(data)

my_list[0], my_list[2] = my_list[2], my_list[0]  # Swap the first and last elements

print(my_list)