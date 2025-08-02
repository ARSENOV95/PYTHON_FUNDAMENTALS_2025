path = input().split("\\")

filename,extension = path[-1].split(".") #since we know the final element of thr
#path is the file name we can split it by the point 
print(f"File name: {filename}")
print(f"File extension: {extension}")