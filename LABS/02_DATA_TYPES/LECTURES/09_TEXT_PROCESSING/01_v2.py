while True:
    input_string = input()

    if input_string == "end":
        break
    
    reverse_string = ''
    for char in reversed(input_string): #reversed only works a with an iterable element if you use it in a for loop for a string it will return it in reverse 
        reverse_string += char

    print(f"{input_string} = {reverse_string}")


    #input 
    #input_string = helLo
    # for char in reversed(input_string):

    #output
   #o
   #L
   #l
   #e
   #h