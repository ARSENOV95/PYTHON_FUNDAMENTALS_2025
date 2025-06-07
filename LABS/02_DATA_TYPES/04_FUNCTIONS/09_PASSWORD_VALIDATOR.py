password = input()

def password_validator(passwd :str):   
    err_counter = False  #flag to check if ther are any errors 
    
    if len(passwd) < 6 or len(passwd) > 10:     #fist check if  the lenght is not in the given interval and set flag to true
        err_counter = True 
        print ("Password must be between 6 and 10 characters" )


    num_digits = 0 #variable to store the number of digits in the password

    for char in passwd:           # loop to check if every cahracter is either alpha or numeric
        if not(char.isalpha() or char.isnumeric()):
            print  ("Password must consist only of letters and digits")
            err_counter = True        # if the characters are not numeric  or alpha set flag to True and end the check loop
            break

        elif char.isnumeric(): #if there is a numeric char count them
            num_digits += 1

    if num_digits < 2:   #final check if the number of digits is less then 2 set flag to True
        err_counter = True    
        print ("Password must have at least 2 digits")

    if err_counter == False:
        print ("Password is valid")


password_validator(password)