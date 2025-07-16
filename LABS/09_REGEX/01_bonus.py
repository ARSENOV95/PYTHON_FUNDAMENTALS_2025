import re

date = input()

pattern = "[0-3][0-9]-[A-Z][a-z]{2}-[0-9]{4}"

matches = re.fullmatch(pattern,date)

print(matches)