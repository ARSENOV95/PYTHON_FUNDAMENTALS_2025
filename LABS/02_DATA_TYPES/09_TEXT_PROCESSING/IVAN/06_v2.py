some_string = input()
final_string = some_string[0] #the finla string will be thefirst character of the original string since it cannot be reprated


for character in some_string:
    if  character != final_string[-1]: #if the current character is != the last symbol of the ifnal string add it 
        final_string += character


print(final_string)