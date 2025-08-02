students  = []
course_to_search = ''

while True:
    students_info = input()

    if ':' not in students_info:
        course_to_search = students_info
        break


    name, id_,courese = students_info.split(':')
    students.append({'name': name,'ID': id_,'course': courese})


    for student in students:
        if course_to_search.startswith(student['course']):
            print(f"{student['name']} - {student['ID']}")