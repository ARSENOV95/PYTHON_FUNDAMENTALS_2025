countries = input().split(", ")
capitals = input().split(", ")

combined_dictionary = {countries[index]:capitals[index] for index in range(len(countries))}

for country,capital in combined_dictionary.items():
    print(f"{country} -> {capital}")