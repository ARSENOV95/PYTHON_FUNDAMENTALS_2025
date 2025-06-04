grade  = float(input())

def print_grade(n):
    if 2.00 <= n <= 2.99:
        return "Fail"
    elif 3.00 <= n <= 3.49:
        return "Poor"
    elif 3.50 <= n <= 4.49:
        return "Good"
    elif 3.50 <= n <= 4.49:
        return "Good"
    elif 4.50 <= n <= 5.49:
        return "Very Good"
    elif 5.50 <= n <= 6.00:
        return  "Excellent"
    else:
        return "None"


print(print_grade(n=grade))