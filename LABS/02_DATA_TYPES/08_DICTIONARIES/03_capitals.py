countries = input().split(", ") #you cannot directly input as list with [input()]
capitals = input().split(", ")

country_capital = {key:val for key,val in zip(countries,capitals)} # you can pars each tuple for the crated zip into a key value 

for key,value in country_capital.items():
    print(f"{key} -> {value}")