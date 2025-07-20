import re

#number of encripted transmissions
number_of_encripted_messages = int(input())
sypher = r"(?i)[star]" #a patternt to count amtch all occurences of the letters s, t, a, r (case insensitive)

# lists to store destroyed and attacked planets
destroyed_planets = [] 
attacked_planets = []

# process each encrypted message
for encription in range(number_of_encripted_messages):
    message = input()   
    decripted_message = ''

    #for every entered message if there is a match for the sypher, pattern count the number of matches
    decription_code = len(re.findall(sypher,message))

    #transform the message by subtracting the decription code from the ASCII value of each character
    for char in message: 
        decipted = ord(char) - decription_code 
        decripted_message += chr(decipted)

    #pattern to decode the message and break them into groups
    decoded_pattern = r"[^@\-\!\:\>]*?@([A-Z][a-z]+)[^@\-\!\:\>]*?:(\d+)[^@\-\!\:\>]*?\!([AD])\![^@\-\!\:\>]*?->(\d+)[^@\-\!\:\>]*?"  
    decoded_message = re.match(decoded_pattern, decripted_message)
    
    #if there is a match, extract the planet name and state by match groups 1 and 3 fro mthe pattern
    if decoded_message:
        planet = decoded_message.group(1)
        state = decoded_message.group(3)

        #if the state is 'A' (attacked) or 'D' (destroyed), add the planet to the respective list
        if state == 'A':
            attacked_planets.append(planet)
        elif state == 'D':
            destroyed_planets.append(planet)

    
print(f"Attacked planets: {len(attacked_planets)}")
if attacked_planets:
    attacked_planets.sort()
    for planet in attacked_planets:
        print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
if destroyed_planets:
    destroyed_planets.sort()
    for planet in destroyed_planets:
        print(f"-> {planet}")
