number_of_symbols = int(input())

for first_char in range(97,97+number_of_symbols):
    for secornd_char in range(97,97+number_of_symbols):
        for third_char in range(97,97+number_of_symbols):
            print(f"{chr(first_char)}{chr(secornd_char)}{chr(third_char)}")