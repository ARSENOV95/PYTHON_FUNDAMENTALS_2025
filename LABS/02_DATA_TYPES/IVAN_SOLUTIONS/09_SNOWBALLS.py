number_of_snowballs = int(input())

max_value = 0
max_weight = 0 
max_time = 0
max_quality = 0

for current_snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quaility = int(input())

    snowball_value = (snowball_weight / snowball_time) **  snowball_quaility

    if snowball_value > max_value:
        max_value = snowball_value
        max_weight = snowball_weight
        max_time = snowball_time
        max_quality = snowball_quaility

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")

