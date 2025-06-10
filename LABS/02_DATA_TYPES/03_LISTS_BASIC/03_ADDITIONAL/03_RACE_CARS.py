from math import floor
from math import ceil

race_distance = input().split()
race_distance = list(map(int,race_distance))

middle_index = floor(len(race_distance)/2) #marks the midlle index of the list  if the list is 11 elements long, it's middle index will be 6-1 = 5
last_index = (len(race_distance)-1) #marks the last index if the list is 11 elements long, the last inde will be 11

#globals to store the sum of both cars 
sum_car_time_one = 0
sum_car_time_two = 0

for car_time_one in range(middle_index): #loop to calculate the sum of the first car , it will loop from 0 to the middle index exclusive

    if race_distance[car_time_one] == 0: 
        sum_car_time_one -= sum_car_time_one* 0.20  #if the distance = 0, decrease tota ltime by 20%
        continue
    
    sum_car_time_one += race_distance[car_time_one] #add the sun to the sum for the first car 

for car_time_two in range(last_index,middle_index, -1):

    if race_distance[car_time_two] == 0:
        sum_car_time_two -= sum_car_time_two* 0.20
        continue
    
    sum_car_time_two += race_distance[car_time_two]

if sum_car_time_one > sum_car_time_two:
    print(f"The winner is right with total time: {sum_car_time_two:.1f}")
else:
    print(f"The winner is left with total time: {sum_car_time_one:.1f}")



    
