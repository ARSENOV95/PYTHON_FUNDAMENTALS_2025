import re

pattern = r'\d+'
numbers = []

while (input_string:= input()) != '':
    match = re.findall(pattern,input_string)
    numbers += match

print(" ".join(numbers))