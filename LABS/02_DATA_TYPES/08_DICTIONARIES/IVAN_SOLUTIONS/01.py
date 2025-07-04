characters = input()
letters = {}

for character  in characters:
    if character == " ":
        continue

    if character not in letters.keys(): 
        letters[character] = 0

    letters[character] += 1

for char, occurance in letters.items():
    print(f"{char} -> {occurance}")

