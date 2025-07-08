filter_words = input().split(", ") # we reciev a string of word which we transfrom into a list (consider the " ")
text = input()


for filter in filter_words: #for each banned word, we iterate trough the text and if found we repalce it with the ban string's lenght 
    while filter in text:
        text = text.replace(filter,"*" * len(filter))

print(text)