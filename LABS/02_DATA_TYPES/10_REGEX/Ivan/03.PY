import re


sentence = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"  #f string can be combined with raw string to create a regex pattern dynamically

matches = re.findall(pattern,pattern,re.IGNORECASE)
print(len(matches))