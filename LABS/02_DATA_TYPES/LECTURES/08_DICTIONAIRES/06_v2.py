initial_string = input().split() #initial string of words word_lower  Java C# PHP PHP JAVA C java

word_count = {} #empty list to store the word count 

for word in initial_string: #loop for every word in the string 
    word_lower = word.lower() #we set the word to lowercase to make the dictionaty case insensiteve 
    if word_lower not in word_count: #if the word is not in the dictionary initally we ste the value to 0 
        word_count[word_lower] = 0
    
    word_count[word_lower] += 1 #and then inceres it by 1, which means every new word will be netered as key and have its value of 0 which we will increase since already in list

for word,count in word_count.items(): #in order to work both with key abd values in a dictionay we use .items() which returns a view of key values

#==view represntation - represents the dictionary times as a list fo several key-value pairs  we iterate trough pair ('java', 3) ...('c', 1) as we would trough  a list
#dict_items([('java', 3), ('c#', 1), ('php', 2), ('c', 1)])

    if count %2 !=0:
        print(word,end = " ") #if the value is an odd number print the results from all iterations in one row

print(word_count.items())
