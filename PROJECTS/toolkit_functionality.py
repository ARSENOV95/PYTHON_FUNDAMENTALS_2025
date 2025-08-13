


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

def valid_input(usr_input :str):
    if usr_input.isnumeric() and int(usr_input) in range(1,10):
        usr_input = int(usr_input)
        return print(f"You have selected option {usr_input}: '{options[usr_input]}'")
    else:
        print("invalid input,please try again")
        num_input_attempts = 3 #onlt promped on wrong input

        while num_input_attempts > 0:
            new_attempt = input()

            if new_attempt.isnumeric() and int(new_attempt) in range(1,10):
                new_attempt = int(new_attempt)
                usr_input = new_attempt
                return print(f"You have selected option {usr_input}: '{options[usr_input]}'")

            num_input_attempts -= 1

        return quit("Number of attempts reached,exiting program.")


def select_choice(choice :str):

    if choice.lower() == 'y':
        return choice
    
    elif choice.lower() == 'n':
        new_choice = input("Would you like to make a new choice Y/N?: ")

        if new_choice.lower() == 'y':
            user_choice  = input()
            if valid_input(user_choice) != "invalid option":
                return user_choice
        elif new_choice.lower == 'n':
            return new_choice
        
    return print("Invalid choice, please try again!")

