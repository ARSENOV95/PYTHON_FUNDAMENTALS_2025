#a dictionary ot store the morse aphabet, by problem description - only the ltters (made it with lowe to be a bit more universal)
morse_alphabet = {
'.-':'a','-...':'b','-.-.':'c',
'-..':'d','.':'e','..-.':'f','--.':'g',
'....':'h','..':'i','.---':'j','-.-':'k',
'.-..':'l','--':'m','-.':'n','---':'o',
'.--.':'p','.-.':'r','...':'s','-':'t',
'..-':'u','...-':'v','.--':'w','-..-':'x',
'-.--':'y','--..':'z'}

#intial coded message 
inital = input() 
encription  = inital.split(' | ') # a list made only for fraagmentign the message inot ltters 

for word in encription: #loop by each word of the ltter 
    letters = word.split() #split the words into letters 
    for letter in letters: 
        if letter in morse_alphabet.keys(): #check if the current letter is in the code alpahbet 
            inital = inital.replace(letter,morse_alphabet[letter].upper(),1) #replace each coded ltter with its upper lating counterpart 

inital = inital.replace(' ','') #remove all bank spaces between the ltters and the | devider
inital = inital.replace('|',' ') #replace the devider with " "

print(inital)
