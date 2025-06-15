string_of_words = input().split()

filtered_words = list(filter(lambda w: len(w) %2 == 0,string_of_words))

for word in filtered_words:
    print(word)

