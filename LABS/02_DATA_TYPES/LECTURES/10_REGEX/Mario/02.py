import re

numbers = input()

regex = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

matches = re.findall(regex,numbers)

for i in range(len(matches)):
    if i < len(matches) - 1: #if not he last index pritnt "number, ""
        print(matches[i],end=', ')
    else:
        print(matches[i]) #else [romt just the number or one row


#print(", ".join(matches))