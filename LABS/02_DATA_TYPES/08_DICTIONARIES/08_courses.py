courses = {} #empty list to store courses and anrolled students 

while (enroll := input()) != "end": #while the entoll command != end 
    course,student = enroll.split(" : ") #split by course and student names 

    if course not in courses.keys(): #if the course is is not in the dictionary, carearte a key with the course name and emty list as value 
        courses[course] = []
    courses[course].append(student) #append the student to the key, each itteration if the key exists only the new stundet will be added ot the list of students 

for course,students in courses.items(): #loop all items from the list
    print(f"{course}: {len(students)}") #for each key- value  pritn the key and the len of the value list
    for student in students: #then to get all students in a new row itterate trough the current value 
        print(f"-- {student}")

    