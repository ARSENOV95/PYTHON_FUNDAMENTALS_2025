intial_text = input().split()

word_count = {}



for word in intial_text:
   word_count[word.lower()] =  word_count.setdefault(word.lower(), 0) +1 


for key,val in word_count.items():
   if val %2 != 0:
      print(key,end = " ")



