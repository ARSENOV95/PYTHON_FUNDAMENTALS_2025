import re

initial_string = input()

mirror_words = []

pattern = r'(?i)([@#])([a-z]{3,})\1{2}([a-z]{3,})\1'  #pattern for finding word pairs with layour #word1##word2# or @word1@@word2@

matches = re.findall(pattern,initial_string) #craate a list with touples with tuples made up fo groups for each match

if matches:
    print(f'{len(matches)} word pairs found!') #if there are matches, then print the count

    for match in matches:   #loop to check if each pair is mirror
        word_1,word_2 = match[1],match[2]

        if word_2 == word_1[::-1]:
            mirror_words.append(f'{word_1} <=> {word_2}') #if yesa ppedn them to the list
    
    if mirror_words: #print the pairs joined as a string by ", "
        print('The mirror words are:')
        print(', '.join(mirror_words))

    else: #if no mirror words p[rint message
        print("No mirror words!")


else: #if no matches, print the no matches output and the no mirror words output as if no matches, then no mirror words
    print("No word pairs found!" )
    print("No mirror words!")

       
