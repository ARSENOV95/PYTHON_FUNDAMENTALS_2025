import re

search_pattern = r'\|([A-Z]{4,})\|\:\#([A-Za-z]+\s{1}[A-Za-z]+)\#'

number_of_inputs = int(input())

for n in range(number_of_inputs):
    user_input = input()

    match = re.search(search_pattern,user_input)

    if match != None:
        print(f'{match.group(1)}, The {match.group(2)}')
        print(f'>> Strength: {len(match.group(1))}\n>> Armor: {len(match.group(2))}')
    else:
        print("Access denied!")
 

