first_string = input()
second_string = input()

while first_string in second_string:
    second_string = second_string.replace(first_string,'')

print(second_string)
#for every itteration we check if the first string is in the second,
#if found replace it wiht '' and store the ne state for the next iteration