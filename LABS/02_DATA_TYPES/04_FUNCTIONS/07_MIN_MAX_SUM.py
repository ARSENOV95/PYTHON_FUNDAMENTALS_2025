def min_max_sum():

    number_sequence = input().split(" ")
    list_of_number = [int(num) for num in number_sequence]

    min_val = min(list_of_number)
    max_val = max(list_of_number)
    sum_numbers = sum(list_of_number)

    return f"The minimum number is {min_val} \nThe maximum number is {max_val} \nThe sum number is: {sum_numbers}"


print(min_max_sum())


        

    
        




