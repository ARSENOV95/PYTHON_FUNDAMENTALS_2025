import re

input_string = input()

num_format = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
               #(^|(?<=\s)) - the number ither is at the beginging of the row ^ or a positive lokkbehind (?<=\s) - checks for zero or 1 occurences of a whitespace
                                                                                                          # whitespace is either = or > 0 -1 
               #-? checs if a - is occured 0 or once in the number - postive or negative 
               #([0]|[1-9][0-9]*)  a group to check if the number is 0 if whole or starts with 0 or das digits startign with 1-9 first 0-9 second and 0 or more currences  of multiple digits
               #(\.\d+)  3rd group - checks if whole number meaning if there is a .3 and so on 
               #($|(?<=\s))' ositive lookahead - checks for the end of the line or a blank space 

matches = re.finditer(num_format,input_string)

for match in matches:
       print(match.group(), end = " ")
