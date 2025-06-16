numbers = input().split(", ")

def positive_numbers(nums :list)-> str:
    return ", ".join([number for number in nums if int(number) >= 0])

def negative_numbers(nums :list)-> str:
    return ", ".join([number for number in nums if int(number) < 0])

def even_numbers(nums :list)-> str:
    return ", ".join([number for number in nums if int(number) %2 == 0])

def odd_numbers(nums :list)-> str:
    return ", ".join([number for number in nums if int(number) %2 != 0])

print(f'Positive: {positive_numbers(numbers)}')
print(f'Negative: {negative_numbers(numbers)}')
print(f'Even: {even_numbers(numbers)}')
print(f'Odd: {odd_numbers(numbers)}')
