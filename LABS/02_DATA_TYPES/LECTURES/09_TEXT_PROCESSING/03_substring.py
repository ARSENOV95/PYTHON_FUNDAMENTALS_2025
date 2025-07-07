lookup_string = input()

string = input()

while lookup_string in string:
    string = string.replace(lookup_string, "")

print(string)