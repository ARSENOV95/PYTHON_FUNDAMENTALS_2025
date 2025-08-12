from math import prod
import re

initial_string = input()

pattern = r'(::|\*\*)([A-Z][a-z]{2,})\1'

coolness = prod([int(char) for char in initial_string if char.isnumeric()]) #creates a list of numbers extracted from the list and multiplies them

emojies = re.findall(pattern,initial_string)

print(f"Cool threshold: {coolness}")
print(f"{len(emojies)} emojis found in the text. The cool ones are:")

for emoji in emojies:

    emoji_coolnes = sum([ord(char) for char in emoji[1]])
    if emoji_coolnes >= coolness:
        print(f"{emoji[0]}{emoji[1]}{emoji[0]}")

