def min_max_sum(numbers :list)->int:

    min_val = min(numbers)
    max_val = max(numbers)
    sum_numbers = sum(numbers)

    return f"The minimum number is {min_val} \nThe maximum number is {max_val} \nThe sum number is: {sum_numbers}"

number_sequence = input().split(" ")
list_of_numbers = [int(num) for num in number_sequence] #converts the intial sequence into numbers

print(min_max_sum(list_of_numbers))


        

    
        




