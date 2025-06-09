def palindrome(string :str)->bool:
        reversed_number = int(string[::-1]) # string splicing is used to reverse the element and covent it int oan integer
        current_number = int(string)

        return  current_number == reversed_number

string_sequence = input().split(', ') # a list of sptrings to split the given numbers into different elements

for current_string in string_sequence:
   print(palindrome(current_string))

