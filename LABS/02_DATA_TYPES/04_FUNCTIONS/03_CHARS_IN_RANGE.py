# a function  in which you enter two parameters  and returns all Unicode symbols between them
def ascii_chars_in_range():      
    ascii_interval = []  

    range_start = ord(input()) + 1
    range_end = ord(input())


    for char in range(range_start,range_end):
        ascii_char  = chr(char)
        ascii_interval.append(ascii_char)

    print(" ".join(ascii_interval))

ascii_chars_in_range()
