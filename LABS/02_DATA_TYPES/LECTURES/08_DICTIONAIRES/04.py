students = []

course = ''


while ":" in (credentials := input()):

    name_,id_,courese_ = credentials.split(":")

    courese_ = courese_.lower()
    id_ = int(id_)

    students.append({"name":name_,
                     "id":id_,
                     "course":courese_
                     })

else:
    course = credentials.lower()


for student in students:
    if course.startswith(student["course"]):
        print(f"{student["name"]} - {student["id"]}")
