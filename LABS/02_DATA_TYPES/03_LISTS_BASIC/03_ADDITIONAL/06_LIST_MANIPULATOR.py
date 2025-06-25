list_nums = list(map(int,input().split()))

while (command := input()) != "end":
    args = command.split()[1:]

    if command.startswith("exchange"):
        index_split_val = int(args[0])

        if index_split_val in range(len(list_nums)):
            first_half = list_nums[:index_split_val+ 1]
            second_half = list_nums[index_split_val+1:]
            list_nums = second_half + first_half
        
        else:
            print("Invalid index")
        
    elif command.startswith("max") or command.startswith("min"):
        if args[0] == "even":
            even_odd = list(filter(lambda x: x%2 == 0,list_nums))
        elif args[0] == "odd":
            even_odd = list(filter(lambda x: x%2 != 0,list_nums))            

        if not even_odd:
            print("No matches")
            continue

        val = max(even_odd) if command.startswith("max") else min(even_odd)
        max_vals = []

        for idx in range(len(list_nums) -1,-1,-1):
            if list_nums[idx] == val:
               max_vals.append(idx)
        
        print(max_vals[0])

    elif command.startswith("first") or command.startswith("last"):
        count = int(args[0])

        if count > len(list_nums):
            print("Invalid count")
            continue

        if args[1] == "even":
            even_odd = list(filter(lambda x: x%2 == 0,list_nums))
        elif args[1] == "odd":
            even_odd = list(filter(lambda x: x%2 != 0,list_nums))

        if not even_odd:
            print([])

        else:
            count_nums = even_odd[0:count] if command.startswith("first") else even_odd[count:]
            if count > len(even_odd):
                count_nums = even_odd
            print(count_nums)

else:
    print(list_nums)
        