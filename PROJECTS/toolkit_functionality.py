#toolkit fucntinoanlty#
#handles logic ofr user promts#

options = {1:"Reverse Text",
           2:"Convert to Uppercase",
           3:"Convert to Lowercase",
           4:"Title Case",
           5:"Count Vowels",
           6:"Remove All Spaces",
           7:"Replace Vowels with '*'",
           8:"Check if Palindrome",
           9:"Word Frequency Counter"
}

num_retries_upon_input_failure = 3


#input validation 
def valid_input(usr_input :str):
    if usr_input.isnumeric() and int(usr_input) in range(1,10): #check if the input is numeric and between 1 inclusive and 10 exclusive
        usr_input = int(usr_input)
        print(f"You have selected option {usr_input}: '{options[usr_input]}'")
        return usr_input #return the value of the code if correct 
         
    else:
        print("invalid input,please try again") #if incorrect give the user 3 attempts at guessing (possibly include an abort function )
        num_input_attempts = num_retries_upon_input_failure #only promped on wrong input (3)

        while num_input_attempts > 0:  #rewuest input while the number of attempts is > 0 
            new_attempt = input()

            if new_attempt.isapha(): #added 14-08-2025 validate if the input is alpha 
                num_input_attempts -= 1
                print ("Input must a number from 1 to 9,")
                continue

            if new_attempt.isnumeric() and int(new_attempt) in range(1,10): #if attept is correct print and return it's value 
                new_attempt = int(new_attempt)
                print(f"You have selected option {new_attempt}: '{options[new_attempt]}'")
                return new_attempt
                 
            num_input_attempts -= 1
            print(f"Invalid input, you have {num_input_attempts} left!")
        #if you run out of attemts abort the program     
        return quit("Number of attempts reached,exiting program.")

#function to prompt action based on desired choice (case insenstive)
# 'y' - return 'y' as value - for  v1 is used as flag 
# 'n' - prompt a reponse from user - if 'n' again exti the program sa user already rekjected his choice once beforehand 
# else - invalid input (possibly add a function to prompt input again?)

def select_choice(choice :str):
    choice = choice.lower().strip() #makes the input case insenstive and removes " ", this is to catch inputs like 'N' and ' n '

    if choice == 'y':
        return choice
    
    elif choice == 'n':
        new_choice = input("Would you like to make a new choice Y/N?: ").lower().strip()

        if new_choice == 'y':
            user_choice  = input()
            return valid_input(user_choice)

        elif new_choice == 'n':
            return quit("Exiting program.")
    
    #case when not Y or N
    print("Invalid choice, please try again!")

    num_input_attempts = num_retries_upon_input_failure
    while num_input_attempts > 0:
        new_choice = input("Please enter 'Y' or 'N' ").lower().strip()

        if new_choice == 'Y':
            return choice
        
        if new_choice == 'N':
            new_choice = input("Would you like to make a new choice Y/N?: ").lower().strip()

        if new_choice == 'y':
            user_choice  = input()
            return valid_input(user_choice)
           
        num_input_attempts -= 1
        print(f"Invalid input, you have {num_input_attempts} left!")

    return quit("Exiting program.")
            
