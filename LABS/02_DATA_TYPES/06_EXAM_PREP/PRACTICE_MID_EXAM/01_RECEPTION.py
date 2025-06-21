fist_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())

num_students = int(input())

students_per_hour =  fist_employee_capacity + second_employee_capacity + third_employee_capacity #TOTAL number of studens per hour

total_hours = 0 #intial hours = 0 as its the start pof the working day

while num_students > 0: #if afer the last hour there are moe students left we stop the loop
    total_hours += 1 # the hour is increase meanign na hour is passed 

    if total_hours %4 == 0: #if the hour is 4th hour the emplyoees are on a break
        continue

    num_students -= students_per_hour #with onre hour passed the numbr of students is decrease by the given capacity

print(f"Time needed: {total_hours}h.")