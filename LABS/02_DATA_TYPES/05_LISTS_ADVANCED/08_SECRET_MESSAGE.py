encripted_messages = input().split(" ")

decoded_message = []

for message in encripted_messages: #every message is dicripted by index
    decripted_word = [] #list to store the dectirpeted characters 
    numeric_part = ' ' #variable to store the numeric part of the message

    for index in range(len(message)):    
        if message[index].isnumeric():
            numeric_part += message[index]  #check if the char is numeric and assign it in the sore variable 
        
        else:
            decripted_word.append(message[index]) #else append it in the decripted list

    #character transformations 
    ascii_conversion = chr(int(numeric_part))  #decripting the first character
    decripted_word.insert(0,ascii_conversion)

    decripted_word[1],decripted_word[-1] = decripted_word[-1],decripted_word[1] #slap of second and last elements 

    message = "".join(decripted_word) #joining again the decoded list into a word and assinging it into a result list 
    decoded_message.append(message) 

decoded_message = " ".join(decoded_message)

print(decoded_message)