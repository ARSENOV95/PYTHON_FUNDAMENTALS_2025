names_list = input().split(", ")

soreted_names = sorted(names_list,key = lambda word: (-len(word),word))
print(soreted_names)
#lambda will be taken as a key for each element of the list, first will will be take -len whic hwill order by lenght desceniding, then it will take by the name asceninding

