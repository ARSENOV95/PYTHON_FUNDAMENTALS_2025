
number_of_offers = list(map(int, input().split(",")))  # convert to integers

number_of_beggars = int(input())

sum_of_offers = []


for beggar_number in range(number_of_beggars):
    sum_offer_accepted = 0

    for offer_number in range(len(number_of_offers)):
        if offer_number % number_of_beggars == beggar_number:
            sum_offer_accepted += number_of_offers[offer_number]
            # print(f"Beggar {beggar_number} accepted offer {number_of_offers[offer_number]} from offer number {offer_number}")
            # Uncomment the above line to see which beggar accepted which offer
        

    sum_of_offers.append(sum_offer_accepted)

print(sum_of_offers) 

