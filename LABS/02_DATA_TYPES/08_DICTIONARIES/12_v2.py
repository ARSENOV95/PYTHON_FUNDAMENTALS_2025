submissions =  {}
count = {}

#submissions = {'java':{'George':10,'Alabala':20},  #visualize the dictionary, how it will loop and optimize for ease of operation
#               'C#':{'Petar':10,'Maria':20}
#               }

while (command := input()) != "exam finished":
    command_parts = command.split('-')

    if command_parts[1] == 'banned':
        user = command_parts[0]
        for curr_language,curr_submission in submissions.items():
            if user in curr_submission.keys():
                curr_submission[user] = 'banned'
        continue


    user,language,points = command_parts
    points = int(points)
    #print(user,language,points) #check 1 - proper split and end of the loop

    #block for submissions
    #case 1 if the language for the curr submission is not in the dictionary - log it
    if language not in submissions.keys():
        submissions[language] = {user:points}
    #case 2 if it is in the submission perform 2 actions
    else:
        #if there is already a submission for the language of a user, check if the current points are smaller than the new submission and replace
        if user in submissions[language].keys():
            if submissions[language][user] == 'banned':
                continue

            elif submissions[language][user] < points:
                submissions[language][user] = points
                continue

        #else create a new submission for th user
        elif user not in submissions[language].keys():
            submissions[language][user] = points
    
    if language not in count.keys():
        count = {language:0}
    count[language] += 1

print("Results:")

for submission in submissions.values():
    for username,points in submission.items():
        if points != 'banned':
            print(f'{username} | {points}')

for language,lan_count in count.items():
    print(f'{language} - {lan_count}')