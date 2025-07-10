file_path = input().split('\\')

for folder in file_path:
    if '.' in folder:
        splitter = folder.index('.')
        
        file_name = folder[:splitter]
        extention = folder[splitter + 1:]
        print(f"File name: {file_name}\nFile extension: {extention}")
                          
