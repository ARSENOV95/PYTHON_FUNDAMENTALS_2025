import re

input_text = input()

#pattern = r'\b^(?!\.-_)([A-Za-z0-9][A-za-z0-9-\._]+)([^\._-]@)\w+((?:-|.).\w+)+\b'

pattern = r'^[A-Za-z0-9]+(?:[._%+-][A-Za-z0-9]+)*@(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}$'

emails = re.findall(pattern,input_text)

print(emails)