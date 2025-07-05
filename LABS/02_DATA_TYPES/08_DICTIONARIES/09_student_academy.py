number_of_students = int(input()) #the number of entries for grades in the acadeny

student_grades = {}

for student in range(number_of_students): #for each entry will enter a nama andd grade 
    name = input()
    grade = float(input())

    if name not in student_grades.keys():
        student_grades[name] = [] #if there is no such student, make an etry in the dictionary witha value an empty list
    student_grades[name].append(grade) #if it exists (even if after it's newly created) and the value to the key

for student in student_grades.keys():
    average_grade = sum(student_grades[student])/len(student_grades[student]) #the average grade will be the sum/number of stored grades 
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")


