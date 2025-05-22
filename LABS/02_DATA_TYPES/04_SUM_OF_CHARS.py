number_of_characters = int(input()) #enter a number between 1 and 20

if number_of_characters < 1 or number_of_characters > 20:
    quit() #edgecase cehck #1 if Number is out of the givenr rage 


sum_of_ascii_codes = 0 #created varaible to store the sum of the postions of every character 

for character in range(number_of_characters):
    new_letter = input() # for each itteration we aentere a new letter
    ascii_code = ord(new_letter) #ord retruns the positoon of an unicode in ascii tables A = 65 and so on
    sum_of_ascii_codes += int(ascii_code) #we add the psotion to the variable and move to the next one 


print(f"The sum equals: {sum_of_ascii_codes}") # after the loop is complete we print the sum of the characters 