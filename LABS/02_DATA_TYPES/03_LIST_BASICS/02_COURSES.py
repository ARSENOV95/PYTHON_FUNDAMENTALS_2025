count_of_number = int(input())

positive_numbers = []
negative_numbers = []



for number in range(count_of_number):
    current_number = int(input())

    if current_number >= 0:
        positive_numbers.append(current_number)
    else:
        negative_numbers.append(current_number)


print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")
