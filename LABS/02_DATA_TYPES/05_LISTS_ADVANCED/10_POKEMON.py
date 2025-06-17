number_sequence = [int(number) for number in input().split(" ")]

list_of_captured_pokemon = []

while number_sequence:
    current_index = int(input())

    if current_index < 0:
        captured_pokemon = number_sequence.pop(0)
        number_sequence.insert(0,number_sequence[-1])

    elif current_index not in range(len(number_sequence)):
        captured_pokemon = number_sequence.pop(-1)
        number_sequence.append(number_sequence[0])

    else:
         captured_pokemon = number_sequence.pop(current_index)

    list_of_captured_pokemon.append(captured_pokemon)

    number_sequence = [num + captured_pokemon if num <= captured_pokemon else num - captured_pokemon for num in number_sequence]


print(sum(list_of_captured_pokemon))



