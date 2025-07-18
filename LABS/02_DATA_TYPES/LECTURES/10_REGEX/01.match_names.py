import re

name = input()

regex = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b" # the "+" searches or for 1 or more chars followig a Captial letter A-Z and a lowercase a-z
matches = re.findall(regex,name)  

#whre \b and \b dermine a boundery - meningi it will return a match if the characters are at the begining or end of the word 
#re.findall  -returns a list with the matches
print(" ".join(matches))