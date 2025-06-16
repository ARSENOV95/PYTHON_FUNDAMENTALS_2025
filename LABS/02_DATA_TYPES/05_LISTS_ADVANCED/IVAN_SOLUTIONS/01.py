first_sequence = input().split()
second_sequence = input().split()

substrings = []

#list elements cant be comared directly  to a list 
#we need to iterate trough both lists anc compare lement by element
#if the first element is in a element from the second list we add it to the substring

for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            substrings.append(first_string)
            break

print(substrings)


