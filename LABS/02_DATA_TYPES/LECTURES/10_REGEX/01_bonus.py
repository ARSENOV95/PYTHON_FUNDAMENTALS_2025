import re

date = input()

pattern = "[0-3][0-9]-[A-Z][a-z]{2}-[0-9]{4}"
           #first digit of the day will be between 0 -3
           #secoind digit between 0-9  29...30 ...
           #then we will have a capital leter from A-Z 
           #occrance of a-z 2 times . and digit from 0-9 4 times to denote ht year 0001 ,1995


matches = re.fullmatch(pattern,date)

print(matches)