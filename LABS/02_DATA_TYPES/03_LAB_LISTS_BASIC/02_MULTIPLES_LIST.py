factor = int(input())
list_length = int(input())

multiples_list = []
multiplier = 1

while len(multiples_list) < list_length:
    multiples_list.append(factor * multiplier)

    multiplier += 1

print(multiples_list)