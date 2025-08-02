title = input()
header = '<h1>\n' + '   ' + title + '\n</h1>'

contents = input()
article  = '<article>\n' + '   ' + contents + '\n</article>'

if header:
    if not article:
        print(header)
    else:
        print(f'{header}\n{article}')

while (command := input()) != "end of comments":
    if command == header or command == article:
        continue

    comment = '<div>\n' + '   ' + command + '\n</div>'
    print(comment)