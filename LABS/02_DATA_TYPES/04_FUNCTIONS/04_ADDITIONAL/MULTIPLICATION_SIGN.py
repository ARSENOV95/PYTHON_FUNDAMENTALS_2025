def multiplicator(nums :list)->str:
    postives = len([num for num in nums if num > 0])
    negatives = len([num for num in nums if num < 0])
    zeroes = len([num for num in nums if num == 0])

    if postives == 3 or negatives == 2:
        print("positive")
    elif negatives %2 != 0:
        print("negative")
    else:
        print("zero")

numbers = [float(number) for number in range(3)]

multiplicator(numbers)