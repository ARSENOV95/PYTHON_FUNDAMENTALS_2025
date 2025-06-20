time_period = 30 #days

#vairables all in kg
total_food= float(input())
total_hay = float(input())
total_cover = float(input())

#waight
weight = float(input())

for day in range(1,time_period + 1):
    if  not (total_food > 0 and total_hay > 0 and total_cover > 0):
        print("Merry must go to the pet store!")
        break

    total_food -= 0.3

    if day %2 == 0:
        total_hay -= total_food * 0.05

    if day %3 == 0:
        total_cover -= weight / 3

else:
    print(f"Everything is fine! Puppy is happy! Food: {round(total_food,2):.2f}, Hay: {round(total_hay,2):.2f}, Cover: {round(total_cover,2):.2f}.")
