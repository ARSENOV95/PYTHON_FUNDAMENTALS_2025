file_path = input().split('\\')

for folder in file_path:
    if '.' in folder:
        splitter = folder.index('.') #find the postion of the do in orde to do slicing 
        
        file_name = folder[:splitter]
        extention = folder[splitter + 1:]
        print(f"File name: {file_name}\nFile extension: {extention}")
                          
