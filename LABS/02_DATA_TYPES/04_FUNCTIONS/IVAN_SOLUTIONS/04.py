def odd_even_sum(sum_number :str) -> str:
    sum_even_numbers = 0
    sum_odd_numbers = 0

    for current_digit in sum_number:
        if int(current_digit) %2 == 0:
            sum_even_numbers += int(current_digit)
        else:
            sum_odd_numbers += int(current_digit)


    return f"Odd sum = {sum_odd_numbers}, Even sum = {sum_even_numbers}"


number = input()

print(odd_even_sum(number))