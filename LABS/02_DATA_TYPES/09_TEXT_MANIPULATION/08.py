def  results(num :int,var :list)->int: #function to calculate the rsult per string in the list 
    first = var[0]
    last = var[-1]

    if first.isupper():
        result = num / (ord(first) - 64)
    elif first.islower():
        result = num * (ord(first) - 96)  
       
    #check for last letter 
    if last.isupper():
        result -= ord(last) - 64         
    elif last.islower():
        result += ord(last) - 96   
    return result

def letters(strings :list)->float:
    total = 0 
    
    for string in strings:
        numbers = int(''.join([x for x in string if x.isnumeric()])) #extract the number from each string 
        
        sum_letters =  results(numbers,string)
        total += sum_letters
    
    return total

initial_string = input().split()

print(f"{letters(initial_string):.2f}")