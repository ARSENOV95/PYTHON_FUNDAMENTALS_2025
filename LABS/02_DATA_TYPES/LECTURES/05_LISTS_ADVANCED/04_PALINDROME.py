def palindrome_counter(words :list,pal :str)->str:
    list_of_palindromes = []
    
    list_of_palindromes = [word for word in words if word == word[::-1]]


    pal_count = list_of_palindromes.count(pal)

    return f"{list_of_palindromes}\nFound palindrome {pal_count} times"
   

text = input().split(" ")
palindrome =  input()


print(palindrome_counter(text,palindrome))