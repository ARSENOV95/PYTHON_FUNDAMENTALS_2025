number_sequence = list(map(int,input().split(", "))) #inital sequnece of numebers as a string, mapped into a new list with all elements as int 

postivies = []
negatives = []
even = []
odd = []

postivies = [num for num in number_sequence if num >= 0] #comprehesion to store elements in a positive or a negative list 
negatives = [num for num in number_sequence if num < 0] #comprehesion to store elements in a positive or a negative list 
even = [num for num in number_sequence if abs(num) %2 == 0]  #comprehesion to store elements in a even or odd list
odd = [num for num in number_sequence if abs(num) %2 != 0] 

large_list = [postivies,negatives,even,odd]

for item in range(len(large_list)):
    large_list[item] = [str(obj) for obj in large_list[item]]

print(f'Positive: {", ".join(large_list[0])}')
print(f'Negative: {", ".join(large_list[1])}')
print(f'Even: {", ".join(large_list[2])}')
print(f'Odd: {", ".join(large_list[3])}')


