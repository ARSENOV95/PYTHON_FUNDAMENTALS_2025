number = input()


def sum_of_digits(input_number : str):
    odd_sum = 0
    even_sum  = 0
    
    for digit in number:
        current_number = int(digit)

        if current_number == 0:
            continue
        elif current_number %2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

print(sum_of_digits(number))