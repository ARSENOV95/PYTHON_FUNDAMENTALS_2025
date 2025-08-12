import toolkit_functionality as utilities

print("Welcome ot the Text Transformation kit!\nChoose a transformation option:" )
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")


#2025-08-12 added input validation
intial_input = input()

utilities.valid_input(intial_input)

confirm_choice = input("Please confirm choice Y/N: ")


confirmation = utilities.select_choice(confirm_choice)
print(confirmation)

if confirmation == 'N':
    quit("Exiting program.")

