text_data = input().split()
new_text = [text * len(text) for text in text_data] 
#creates a new list with stings multiplied by their lenght

print(''.join(new_text))