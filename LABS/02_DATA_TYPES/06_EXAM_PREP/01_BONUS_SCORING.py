from math import ceil

number_of_students = int(input())
number_of_lecures = int(input())
addtional_bonus = int(input())

max_bonus = 0 #the max bonus cannot be zero or negative
attendence = 0

if number_of_students:
    for student in range(number_of_students):

        attended_lecures = int(input())

        if attended_lecures > number_of_lecures:
            ("Invalid number of lectures")
            break

        total_bonus = attended_lecures / number_of_lecures* (5 + addtional_bonus)

        if total_bonus > max_bonus:
            max_bonus = total_bonus
            attendence = attended_lecures


print(f"Max Bonus: {ceil(max_bonus)}.\nThe student has attended {attendence} lectures.")
