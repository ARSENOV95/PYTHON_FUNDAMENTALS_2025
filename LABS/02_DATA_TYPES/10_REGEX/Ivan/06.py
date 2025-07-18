import re
pattern = r"(w{3}.[A-Za-z0-9\-]+(\.[a-z]+)+)"

line = input()
while line:
    matches = re.search(pattern, line)
    if matches:
       link = matches.group(1)
       print(link)
    line = input()

