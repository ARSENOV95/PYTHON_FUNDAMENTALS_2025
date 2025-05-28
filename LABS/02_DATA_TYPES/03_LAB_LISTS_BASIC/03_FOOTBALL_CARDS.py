player_red_cards = input()

set_of_red_cards = set(player_red_cards.split()) # a set to store unique red cards ,a player acannot be kicked out twice
list_of_red_carts = list(player_red_cards) 

number_of_players  = 11
cards_a_team = 0
cards_b_team = 0
game_terminated = False

for red_card in list_of_red_carts:

    if red_card.startswith("A"):
        cards_a_team += 1
    elif red_card.startswith("B"):
        cards_b_team += 1

    if cards_a_team > 4 or cards_b_team > 4:
        game_terminated = True
        break
   

print(f"Team A - {number_of_players - cards_a_team}; Team B - {number_of_players - cards_b_team}")
if game_terminated:
    print("Game was terminated")

