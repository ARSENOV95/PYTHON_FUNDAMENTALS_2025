number_of_strings = int(input())

magic_word = input()

strings = [input() for string in range(number_of_strings)] 
filtered_strings = [current_string for current_string in strings if magic_word in current_string]

print(f"{strings} \n{filtered_strings}")