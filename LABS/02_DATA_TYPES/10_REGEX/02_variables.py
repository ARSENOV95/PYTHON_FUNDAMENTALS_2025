import re

string = input()
variables = []

pattern = r'[_][A-Zaa-z0-9]+'

matches = re.findall(pattern,string)

for match in matches:
    x = re.sub("_",'',match)
    variables.append(x)

print(','.join(variables))