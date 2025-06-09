def password_validator(some_password :str) -> list:
    list_with_errors = []

    if len(some_password) not in range(6,10):
        list_with_errors.append("Password must be between 6 and 10 characters")
    
    if not some_password.isalnum():
        list_with_errors.append("Password must consist only of letters and digits")
    
    digits_counter = 0

    for current_character in some_password:
        if current_character.isdigit():
            digits_counter += 1

    if digits_counter < 2:
        list_with_errors.append("Password must have at least 2 digits")


    return list_with_errors


password = input()

error_messages = password_validator(password)

if not error_messages: #no errors and no error list is created
    print("Password is valid")

else:
    print("\n".join(error_messages)) #print all errors form the list with a new row 