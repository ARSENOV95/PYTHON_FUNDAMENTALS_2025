contest_pass = {}
user_contests = {}

max_score = 0
user_with_max_score = ''

while True:
    contest_data = input()

    if contest_data == 'end of contests':
        break

    contest, password = contest_data.split(':')
    contest_pass[contest] = password

while True:
    user_data = input()

    if user_data == 'end of submissions':
        break

    contest, password, username, points = user_data.split('=>')
    points = int(points)

    if not (contest in contest_pass.keys() and password == contest_pass[contest]):
        continue

    if username not in user_contests:
        user_contests[username] = {}

    if contest not in user_contests[username].keys():
        user_contests[username].update({contest: points})
    elif user_contests[username][contest] < points:
        user_contests[username][contest] = points


for user,contest_points in user_contests.items():
    points_per_contestant = 0
    for contest,points in contest_points.items():
        points_per_contestant += points

    if points_per_contestant > max_score:
        max_score = points_per_contestant
        user_with_max_score = user

print(f"Best candidate is {user_with_max_score} with total {max_score} points.")

print("Ranking:")

for user,contest_points in sorted(user_contests.items()):
    print(user)
    for contest,points in sorted(contest_points.items(),key = lambda x:x[1], reverse=True):  ##lambda x:x[1] uses 1 as a placeholder for the dict value, for decneing we use the reverse
        print(f'#  {contest} -> {points}')
