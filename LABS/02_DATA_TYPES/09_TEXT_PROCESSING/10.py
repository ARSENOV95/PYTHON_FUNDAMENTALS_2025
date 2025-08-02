def is_valid(tick :str)->bool:
    return len(tick) == 20

def check_special(chr :str,str_part: str)-> int:
    count = 0
    for i in range(0,len(str_part)):
        if str_part[i] == chr and count == 0:
            count += 1
        elif str_part[i] == chr and str_part[i] == str_part[i -1]:
            count += 1 
    return count

special = ['@','#','$','^']

tickets = input().split(",")
     
for ticket in tickets:
    ticket = ticket.strip()
    
    winnings = 0
    is_winner = False

    if not is_valid(ticket):
        print("invalid ticket")
        continue

    for char in special:

        if not (char in ticket):
            continue

        first_half = ticket[:10]
        second_half = ticket[10:]
        count_first_half = 0 
        count_second_half = 0

        count_first_half = check_special(char,first_half)
        count_second_half = check_special(char,second_half)

        if count_first_half >= 6 and count_second_half >= 6:
            
            is_winner = True
            winnings = min(count_first_half,count_second_half)
            break

    if is_winner:
        if winnings == 10:
            print(f'ticket "{ticket}" - {winnings}{char} Jackpot!')
        elif 6 <= winnings <= 9:
            print(f'ticket "{ticket}" - {winnings}{char}')
    else:
        print(f'ticket "{ticket}" - no match')
