import re

input_string = input()
lookup = input()
pattern = r'\b' + lookup + r'\b'  #build the regex as a string surrounf it by two r'' and concating it with the two parts of the regex

match = re.findall(pattern,input_string,re.IGNORECASE)


print(len(match))