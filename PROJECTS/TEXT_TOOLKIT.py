print("Welcome ot the Text Transformation kit!\nChoose a transformation option" )
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")


user_choice = int(input("Please enter the number of the option you like to choose: "))

#ask to confirm choice
text_entry = input("Please input text: ")

text_result = ''

confirm_choice = input("Please confirm your choice with Y/N: ")
if confirm_choice == 'N':
    final_confirmation = input("Would you like to make a new choice Y/N?: ")
    if final_confirmation == 'Y':
        user_choice  = int(input("Please enter the number of the option you like to choose: "))
    else:
        print("Have a great day!")
        quit()

if user_choice == 1:
    text_result = text_entry[::-1]

elif user_choice == 2:
    if text_entry.isupper():
        print("Text is aready in Upper Case!")
        quit()

    text_result = text_entry.upper()

elif user_choice == 3:
    if text_entry.islower():
        print("Text is aready in Lower Case!")
        quit()

    text_result = text_entry.lower()

elif user_choice == 4:
    if text_entry.istitle():
        print("Text is aready in Title Case!")
        quit()

    text_result = text_entry.title()

elif user_choice == 5:


    vowels = 'aeiou'
    vowels_count = 0

    for letter in text_entry:
        if (letter in vowels) or (letter in vowels.upper()):
            vowels_count += 1
    

    if vowels_count == 0:
        text_result = "The given text has no vowels"
    else:
        text_result = vowels_count

elif user_choice == 6:
    pass

print(text_result)

