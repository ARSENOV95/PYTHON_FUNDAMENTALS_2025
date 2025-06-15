string_of_words = input().split()

flitered_words = [word for word in string_of_words if len(word) %2 == 0]

for word in flitered_words:
    print(word)
