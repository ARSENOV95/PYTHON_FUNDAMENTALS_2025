#creates a string from list elements
user_data = input().split() #input: "John Doe"

fist_name,last_name = user_data  #first_name = "John", last_name = "Doe"
print(f"{fist_name}\n{last_name}")

#this is called list unpacking, when you unpack a list index into multiple variables

#joins the two elemets of the list into a single string
user_names = " ".join(user_data)  #user_names = "John Doe"
print(user_names)  #prints: John Doe

#join accepts strings as input 
