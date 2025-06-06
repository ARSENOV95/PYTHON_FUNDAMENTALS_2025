number_sequence = input().split(" ")

list_of_numbers = [int(number) for number in number_sequence]

print(sorted(list_of_numbers)) 
# by default sorted sorts in ascending order 