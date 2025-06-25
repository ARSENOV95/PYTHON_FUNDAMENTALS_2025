from math import ceil

budget = float(input())
students = int(input())
flour_price  = float(input())
price_per_egg = float(input())
price_per_aprons = float(input())

eggs_per_student = 10
number_of_aprons =  students + ceil((students * 0.20))

total_flour_price = flour_price * students
total_egg_cost = (eggs_per_student * students) * price_per_egg
total_price_aprons = number_of_aprons * price_per_aprons

free_packages  = sum(pack for pack in range(1,students + 1) if pack %5 == 0)

course_products_cost = (total_flour_price - (free_packages * flour_price)) + total_egg_cost + total_price_aprons


if course_products_cost <= budget:
    print(f"Items purchased for {course_products_cost:.2f}$.")
else:
    print(f"{(abs(budget - course_products_cost)):.2f}$ more needed.")

