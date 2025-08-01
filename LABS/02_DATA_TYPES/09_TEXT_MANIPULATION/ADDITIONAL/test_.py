from math import prod

import re

coolness_threshold = 0 

emoji_pattern = r'([::|\*\*])([A-Z][a-z]{2,})\1'



emojis = input()

coolness_threshold  = prod([int(char) for char in emojis if char.isnumeric()])
matches = re.findall(emoji_pattern,emojis)

print(f"Cool threshold: {coolness_threshold}")


print(f"{len(matches)} emojis found in the text. The cool ones are:")

for match in matches:
    coolness = 0
    for char in match[1]:
       coolness +=  ord(char)

    if coolness >= coolness_threshold:
        print(f"{match[0]}{match[1]}{match[0]}")

