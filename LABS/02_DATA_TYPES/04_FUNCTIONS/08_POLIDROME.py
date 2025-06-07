number_sequence = input().split(', ') # a list of sptrings to split the given numbers into different elements


def palindrome(squence):

    for number in number_sequence: # for every element
        is_palindrome = False  #falg variable to see if the number is a palindrome
    
        reversed_number = int(number[::-1]) # string splicing is used to reverse the element and covent it int oan integer
        current_nnumber = int(number)

        if current_nnumber == reversed_number:
            is_palindrome = True
    
        print(is_palindrome)


palindrome(number_sequence)
