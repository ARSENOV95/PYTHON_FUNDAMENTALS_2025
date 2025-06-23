time_period = 30 #days

#vairables all in kg
total_food= float(input()) * 1000
total_hay = float(input()) * 1000
total_cover = float(input()) * 1000

#waight
weight = float(input()) * 1000

if not (total_food > 0 and total_hay > 0 and total_cover > 0):
    print("Merry must go to the pet store!")


for day in range(1,time_period + 1):
    if  not (total_food > 0 and total_hay > 0 and total_cover > 0):
        print("Merry must go to the pet store!")
        break

    total_food -= 300

    if day %2 == 0:
        total_hay -= total_food * 0.05

    if day %3 == 0:
        total_cover -= weight / 3

else:
    print(f"Everything is fine! Puppy is happy! Food: {total_food/1000:.2f}, Hay: {total_hay/1000:.2f}, Cover: {total_cover/1000:.2f}.")
