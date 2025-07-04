number_of_words = int(input())

list_of_synonyms = {}

for i in range(number_of_words):
    word = input()
    synonym = input()

    if word not in list_of_synonyms:
        list_of_synonyms[word] = [] #in this way we assing a the key to be an empty list if not in the dictionary

    list_of_synonyms[word].append(synonym) #afterwars 1 if nto in the dictionary it will be an empty list and the fust encounter wuill be appended ot the list 

   #in short to be able to asign every key to have a value - list, we need tyo define it to be = [] first if not present and then append a value to it
for synonym in list_of_synonyms:
    print(f"{synonym} - {', '.join(list_of_synonyms.get(synonym))}") #using only the key form a dictionary we ittereate trough it and for to get the list we use the
    #.get method