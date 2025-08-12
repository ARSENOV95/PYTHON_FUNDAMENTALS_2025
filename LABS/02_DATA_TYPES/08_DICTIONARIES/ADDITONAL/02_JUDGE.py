contests = {} #stores courese and users
participent_points = {}

while (command:= input()) != "no more time":
    information = command.split(" -> ")
    username,contest = information[:2]
    points = int(information[2])

    if contest not in contests.keys():
        contests[contest] = {username:points}
    else:
        if username not in contests[contest].keys():
            contests[contest][username] = points
        elif contests[contest][username] < points:
            contests[contest][username] = points
    
#print(contests)  

#displays number of participents per courese 
for course,participents in contests.items():
    print(f"{course}: {len(participents)} participants")
    ranking = 1
    for user,points in sorted(participents.items(),key = lambda x: x[1],reverse = True):
        print(f'{ranking}. {user} <::> {points}')
        ranking += 1

        #tired a method for calcualting tital points of a user by using a dictionary
        if user not in participent_points.keys():
            participent_points[user] = points
        else:
             participent_points[user]  += points

print("Individual standings:")

ranking = 1
for user,points in sorted(participent_points.items(),key= lambda x: x[1],reverse=True):
    print(f"{ranking}. {user} -> {points}")
    ranking += 1