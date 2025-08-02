course_students = []

course = ''


while True:
    command = input()

    if ':' not in command:
        course = command
        break

    student,id,subject = command.split(':')
    course_students.append({'student':student,'id':id,'course':subject,})


for info in course_students:
    if course == info['course'] or course.startswith(info['course'][:5]):
        print(f"{info['student']} - {info['id']}")

        