def vowels_check(words :str)->str:

    vowels = ['a','e','i','o','u'] # a list of volew which we used for checking each letter form the entered word 
    n_vowels = [letter for letter in words if letter.lower() not in vowels]  
    #append a letter from a string when it's lowercase conversion is not in sthe string of vowels 
    #why,  beacuse if we convert the letter to lowe in the if condition we can make it case insensitive 

    return print("".join(n_vowels)) #the result should be a print 

string = input()

vowels_check(string)
