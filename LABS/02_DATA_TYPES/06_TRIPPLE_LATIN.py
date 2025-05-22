number_of_letters = int(input())  #3

small_letters = 96 #index for finding the position


for letter_one in range(1,number_of_letters + 1): #the rane will be form index 0 to 2
    letter_one += small_letters    #we add the index to the intial value to recieve the index for the current ASCII character 1 + 96 = 97"a", ..98 "b"
    for letter_two in range(1,number_of_letters + 1): 
            letter_two += small_letters      #we do the same for all nested loops to recieve a combination fo 3 characters 
            for letter_three in range(1,number_of_letters + 1):     
                letter_three += small_letters
                print(f"{chr(letter_one)}{chr(letter_two)}{chr(letter_three)}")      #prints put the ASCII symbol for every combintation of the loops

