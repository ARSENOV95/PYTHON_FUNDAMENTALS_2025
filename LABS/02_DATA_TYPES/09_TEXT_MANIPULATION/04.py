message_input = input()
decripted = ''

for char in message_input:
    encripted = ord(char) + 3
    decripted += chr(encripted)
    
print(decripted)