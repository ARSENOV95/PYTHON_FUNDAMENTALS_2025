party_size = int(input())
advenure_lenght_days = int(input())


total_coins_earned = 0 

for day in range(1,advenure_lenght_days + 1):
    coins_per_day = 50

    if day %10 == 0:
        party_size -= 2
    
    if day %15 == 0:
        party_size += 5


    coins_per_day -= (party_size * 2)

    if day %3 == 0:
        coins_per_day -= (party_size * 3)

    if day %5 == 0:
        coins_per_day += (party_size * 20)
        if day %3 == 0:
           coins_per_day -= (party_size * 2)

    
    total_coins_earned += coins_per_day

print(f'{party_size} companions received {int(total_coins_earned/party_size)} coins each.')

