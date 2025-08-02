string = input()

prev_char = '' #var to store the prvious character 
final = '' # a sting to store the final state of the inital string 

for char in string:  
    if char != prev_char: # if the character is != the nthe privious one add it to the final 
        final += char

    prev_char = char 

print(final)

#example
#aaaaabbbbbcdddeeeedssaa   
#prev = '' char = a is char != prev  yes, then final = a and prev = a
#prev = 'a' char = a  is char != prev no, then skip while all the "a" are paseed torug the loop
#prev = 'a' char = b is char != prev  yes, then final = 'ab' and prev = b
#prev = 'b' char = b  is char != prev no, then skip while all the "b" are paseed torug the loop
#prev = 'b' char = c  is char != prev yes, then final = 'ab' and prev = c
