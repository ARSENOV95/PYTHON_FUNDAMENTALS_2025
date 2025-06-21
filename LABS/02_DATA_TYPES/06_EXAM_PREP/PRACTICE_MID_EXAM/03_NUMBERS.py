numbers = [int(num) for num in input().split()]

average = sum(numbers)/len(numbers)


bigger_then_average = list(filter(lambda x: x > average,numbers))


if bigger_then_average:
    bigger_then_average.sort(reverse= True)
    bigger_then_average = bigger_then_average[:5] # cuts the sorted list to the 4th Index + 1 (inclusive) to get the top 5 elements 
    print(" ".join([str(num) for num in bigger_then_average]))
else:
    print("No")
                                            