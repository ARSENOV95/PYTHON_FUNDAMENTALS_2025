phone_book = {}

while True:
    entry = input()

    if "-" not in entry:
        break

    name,number = entry.split("-")

    phone_book[name] =  number


searches = int(entry) #if we recive a value without - it will be saved i nthe memeory 
#and we will append it 

for search in range(searches):
    searched_name = input()

    if searched_name in phone_book.keys():
        print(f"{searched_name} -> {phone_book[searched_name]}")
    else:
        print("Contact {searched_name} does not exist")