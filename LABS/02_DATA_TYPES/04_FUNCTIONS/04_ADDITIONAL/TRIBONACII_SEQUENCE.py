def tribunacii_sequence(nums :int)->list:

    sequence = [1] # first number of the sequence is always one 

    #for the lenght of the sequence loop 
    for i in range(nums - 1):  #since we ahave the first number will loop trought the len of the sequence - 1
        if len(sequence) < 3: # if the len is < 3 the next sequence will be the sum of the whole list
            next_num = sum (sequence)
        else: #else it will be the um of the last 3 numbers 
            next_num = sum (sequence[-3:])
        
        sequence.append(next_num)

    return ' '.join([str(x) for x in sequence]) 

seq_len = int(input())

print(tribunacii_sequence(seq_len))