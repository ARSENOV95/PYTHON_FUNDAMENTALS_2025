statistics = {}

while (entry := input()) != "exam finished":

    entry = entry.split("-")

    if entry[1] == "banned":
        for value in statistics.values():
            if entry[0] in value[0].keys():
               del value[0][entry[0]]
        continue

    username,language,points = entry
    
    if language not in statistics.keys():
         statistics[language]  = [{},0]

    if username not in statistics[language][0].keys():
        statistics[language][0].update({username:points})
    elif statistics[language][0][username].values() < points:
       statistics[language][0][username] = points
    statistics[language][1] += 1   

print("Results:")

for value in statistics.values():
    for key,val in value[0].items():
        print(f"{key} | {val}")
print("Submissions:")

for key in statistics.keys():
    print(f"{key} - {statistics[key][1]}")


   


