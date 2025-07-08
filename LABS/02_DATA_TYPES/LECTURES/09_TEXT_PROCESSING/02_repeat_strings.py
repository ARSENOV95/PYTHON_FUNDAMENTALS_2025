input_string = input().split()# in case of several substring devided by space we split the string into a list


result = '' #a varable to store the manipulated string

for string in input_string:
    string_lengh = len(string)  #we need to  multiply each string by  number of characters in its leght 'ab' len(ab) = 2  result = 'ab' * 2 = "abab"
    result += string * string_lengh # we append each multipied substring to the result variable 

print(result)