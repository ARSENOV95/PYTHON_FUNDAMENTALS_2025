import re

locations = input()

filter_pattern = r'([=\/])([A-Z][A-Za-z]{2,})\1'

list_of_locations = re.findall(filter_pattern,locations)

destinations = [dest[1] for dest in list_of_locations]
print(f"Destinations: {', '.join(destinations)}")

points =  sum([len(dest[1]) for dest in list_of_locations])
print(f"Travel Points: {points}")


