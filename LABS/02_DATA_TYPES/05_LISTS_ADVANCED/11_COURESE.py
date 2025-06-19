list_of_courses = input().split(",")

while (command := input()) != "course start":
    instruction,*args = command.split(":")
    course = args[0]
    index = int(args[1]) if len(args) > 1 else 0

    for course_position in range(len(list_of_courses)):

