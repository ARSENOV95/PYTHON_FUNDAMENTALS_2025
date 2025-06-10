money_as_string = input().split(", ")
number_of_beggers = int(input())

final_list = []

money_as_int = [int(money) for money in money_as_string]

#for current_money in money_as_string:
#    money_as_int.append(current_money)

start_index = 0

for begger in range(number_of_beggers):
    sum_money = 0
    for index in range(start_index,len(money_as_int),number_of_beggers):
        sum_money += money_as_int[index]


    start_index += 1

    final_list.append(sum_money)

print(final_list)


