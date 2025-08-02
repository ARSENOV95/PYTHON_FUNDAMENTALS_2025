message_input = input()
decripted = ''

for char in message_input:
    decripted += chr(ord(char)+ 3) 
 
print(decripted)