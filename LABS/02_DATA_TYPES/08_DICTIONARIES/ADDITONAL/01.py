contest_pass = {}
user_contests = {}

max_score = 0
user_with_max_score = ''

while True:
    contest_data = input()

    if contest_data == 'end of contests':
        break

    contest,password = contest_data.split(':')
    contest_pass[contest] = password

while True:
    user_data = input()

    if user_data == 'end of submissions':
        break

    contest,password,username,points = user_data.split('=>')
    points = int(points)

    if  not (contest in contest_pass.keys() and password == contest_pass[contest]):
        continue

    if username not in user_contests:
        user_contests[username] = []

    if contest not in user_contests[username]:
        user_contests[username].append({contest:points})
    
    elif user_contests[username][contest] < points:
        user_contests[username][contest] = points

   
for key,value in user_contests.items():
    points_per_contestant = 0
    for val in value:
        for val1 in val.values():
            points_per_contestant += val1
    if points_per_contestant > max_score:
        max_score = points_per_contestant
        user_with_max_score = key

print(f"Best candidate is {user_with_max_score} with total {max_score} points.")

print("Ranking:")

for key,value in sorted(user_contests.items()):
    print(key)
    for contest_points in value:
        for contest,poits in contest_points.items():
            print(f"#  {contest} -> {poits}")



