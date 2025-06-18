list_of_courses = input().split(", ")

while (command := input()) != "course start":

    action,*args = command.split(":")
    current_course  = args[0]

    if len(args) > 1 and args[1].isnumeric():
        position = int(args[1])
    elif len(args) > 1 and args[1].isalpha():
        second_course = args[1]

    if action == 'Add' and current_course not in list_of_courses:
        list_of_courses.append(current_course)

    elif action == 'Insert' and current_course not in list_of_courses:
        list_of_courses.insert(position,current_course)

    elif action == 'Remove' and current_course in list_of_courses:
        #if the current course has an exercise, remove that as well
        if (ex_val :=current_course+"-Exercise") in list_of_courses:
            list_of_courses.remove(ex_val)

        list_of_courses.remove(current_course)

    elif action == 'Swap'and (current_course in list_of_courses and second_course in list_of_courses):
        first_course_pos = list_of_courses.index(current_course)
        second_course_pos = list_of_courses.index(second_course)

        #locating and storing positons of exercises if any
        ex1 = current_course+"-Exercise" if current_course+"-Exercise" in list_of_courses else ''
        ex2 = second_course+"-Exercise" if second_course+"-Exercise" in list_of_courses else ''
        index1 = list_of_courses.index(ex1) if ex1 != '' else 0
        index2 = list_of_courses.index(ex2) if ex2 != '' else 0

        list_of_courses[first_course_pos],list_of_courses[second_course_pos] = list_of_courses[second_course_pos],list_of_courses[first_course_pos]

        if ex1 != '' and ex2 == '':
            list_of_courses.pop(index1)
            list_of_courses.insert(second_course_pos + 1,ex1)

        elif ex2 != '' and ex1 == '':
            list_of_courses.pop(index2)
            list_of_courses.insert(first_course_pos + 1,ex2)

        elif ex1 != '' and ex2 != '':
            list_of_courses[index1],list_of_courses[index2] = list_of_courses[index2],list_of_courses[index1]
 
    elif action == 'Exercise':
        if current_course not in list_of_courses and current_course+"-Exercise" not in list_of_courses:
            list_of_courses.append(current_course)
            list_of_courses.append(current_course+"-Exercise")

        elif current_course in list_of_courses and current_course+"-Exercise" not in list_of_courses:
            course_position = list_of_courses.index(current_course)
            list_of_courses.insert(course_position +1,current_course+"-Exercise")


curr_course = 1

for index in range(len(list_of_courses)):
    course = list_of_courses[index]
    if list_of_courses.count(course) > 1:
        continue

    print(f"{curr_course}.{list_of_courses[index]}")
    curr_course += 1






