import re

names = input()
string = input()

racers= {}

while string != 'end of race':
    name = re.findall(r"([A-Za-z]+)",string)
    distance = re.findall(r"([\d])",string)

    racer = ''.join(name)
    racer_distance = sum(int(x) for x in distance)
    
    if racer in names.split(", ") and racer_distance > 0:
        if racer not in racers:
            racers[racer] = 0
        racers[racer] += racer_distance

    string = input()

place = 1

for racer,distance in  sorted(racers.items(), key=lambda x: (-x[1], x[0])):  
    if place == 1:
        print(f"1st place: {racer}")
    elif place == 2:
        print(f"2nd place: {racer}")    
    elif place == 3:
        print(f"3rd place: {racer}")

    place += 1
