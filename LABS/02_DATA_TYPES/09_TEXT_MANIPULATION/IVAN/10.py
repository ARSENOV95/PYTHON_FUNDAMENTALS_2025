def check_ticket (ticket:str)->str:
    if len(ticket) != 20:
        return "Invalid ticket" #if the 20 <ticket < 21 return Ivnalid ticket else continei function 

    match_symbol = ('@', '#','$','^')
    left_part = ticket[:10]
    right_part = ticket[:10]

    for winning_symbol in match_symbol:
        for uninterurupted_match_lenght  in range(10,5,-1): #iterratetews torugh the  possible repetiton for winning cases
            winning_symbol_reptition =  match_symbol * uninterurupted_match_lenght
            #$$$$$$$$ or #$$$$$$$
            if winning_symbol_reptition in left_part and\
            winning_symbol_reptition in right_part:
                if uninterurupted_match_lenght == 10:
                    return f'ticket "{ticket}"  - {uninterurupted_match_lenght}{winning_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterurupted_match_lenght}{match_symbol}'
    # if there is no winning symobl in both half  we exti the loo pand return no match
    return f'ticket "{ticket}" - no match' # if no winning symbol but valid - no match

tickets = [ticket.strip() for ticket in input().split(", ")] #dirctly sprilts and removed white spaces 

for current_ticket in tickets:
    print(check_ticket(current_ticket))