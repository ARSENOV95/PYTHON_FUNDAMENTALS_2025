import re

line = input()

while line:
    pattern = r"\d+"

    matches = re.findall(pattern,line)
    if matches: #if there is  a match 
       print(" ".join(matches),end = " ") #print the match values on a single row 
    line = input()