words = input().split(' ')
palindrome = input()

palindrome_list = [word for word in words if word == words[::-1]]
pal_count = palindrome_list.count(palindrome)

f"{palindrome_list}\nFound palindrome {pal_count} times"