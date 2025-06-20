numbers = [int(num) for num in input().split()]

average = sum(numbers)/len(numbers)
print(average)

bigger_then_average = list(filter(lambda x: x > average,numbers))
print(bigger_then_average)

if bigger_then_average:
    bigger_then_average.sort(reverse= True)
    bigger_then_average = bigger_then_average[:4]
    print(" ".join([str(num) for num in bigger_then_average]))
else:
    print("No")
                                            