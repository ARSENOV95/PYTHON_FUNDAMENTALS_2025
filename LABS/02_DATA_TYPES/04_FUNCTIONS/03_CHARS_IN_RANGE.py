# a function  in which you enter two parameters  and returns all Unicode symbols between them
def ascii_chars_in_range(start :str,end :str) -> list:      
    ascii_interval = []  

    for char in range(start,end):
        ascii_char  = chr(char)
        ascii_interval.append(ascii_char)

    return (" ".join(ascii_interval))

range_start = ord(input()) + 1
range_end = ord(input())


print(ascii_chars_in_range(range_start,range_end))


