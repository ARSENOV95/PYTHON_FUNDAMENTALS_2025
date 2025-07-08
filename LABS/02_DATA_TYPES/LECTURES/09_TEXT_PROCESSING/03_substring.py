lookup_string = input()

string = input()

while lookup_string in string: #if a substring is in a string we need to loop toruigh the string until the last occurance is removed
    string = string.replace(lookup_string, "") #each itteration will replace the string with itself  with removed lookup value with ""

#the loop will end once the lookup value  is not encountered in the string 
print(string)