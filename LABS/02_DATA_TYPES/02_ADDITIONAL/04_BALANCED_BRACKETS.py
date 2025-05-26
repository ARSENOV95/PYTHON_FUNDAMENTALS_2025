number_of_strings = int(input())


count_of_brackets = 0
is_balanced = True

previous_string = ""
list_of_brackets = []

for current_string in range(number_of_strings):
    new_string = input()

    if new_string == "(" or new_string ==")":
        count_of_brackets += 1
        list_of_brackets.append(new_string)

        if new_string == previous_string:
            is_balanced = False

        if new_string == ")" and "(" not in list_of_brackets:
            is_balanced = False

        previous_string = new_string


if count_of_brackets %2 != 0:
    is_balanced = False

    
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
    
