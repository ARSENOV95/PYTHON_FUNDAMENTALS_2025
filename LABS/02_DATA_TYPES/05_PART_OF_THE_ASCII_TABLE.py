first_postion = int(input()) #first postion of the ASCII table to be looped  
last_posistion = int(input()) #last postion of the ASCII table to be looped

#example values 60
#example values 65


for index in range(first_postion,last_posistion +1):
                         #60 to 65(exclusive) + 1

    ascii_symbol = chr(index)  #prisnt the sybol for index 60...65 of the ASCII TABLE
    print(ascii_symbol, end = " ")
