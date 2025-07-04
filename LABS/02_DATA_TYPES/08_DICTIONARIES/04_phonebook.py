phonebook = {}
attempts = 0

while True:
    contact = input().split("-")
    
    if 0 < len(contact) < 2 and contact[0].isnumeric():
        attempts = int(contact[0])
        break

    name,number = contact
    phonebook[name] = number


for attempt in range(attempts):
    contact_lookup = input()
    match = phonebook.get(contact_lookup)

    if match:
        print(f"{contact_lookup} -> {phonebook[contact_lookup]}")
    else:
        print(f"Contact {contact_lookup} does not exist.")



    