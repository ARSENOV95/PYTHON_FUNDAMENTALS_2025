import re

num_lines = int(input())

#set up trow regex aptters to check for names and ages (to avoid unwated input we group the name and ages between the two given sibles but we do not include thme)
name_pattern = '(?i)@([a-z]+)\|'
name_patter = '#(\d{1,})\*'

search_patterns = [name_pattern,name_patter] # we insert both patterns in a list 

for line in range(num_lines):
    curr_line = input()
    matches = []

    #for each entered line we loop trough the aptterns and append the result in a list we should only have one name and age per linr
    for pattern in search_patterns:
        match = re.search(p,curr_line)
        matches.append(match.group(1))

    #print(f"{matches[0]} is {matches[1]} years old.")
