# Program: Find Number of Lines in File
with open("file_operations/1_prog.txt", 'r') as file:
    content = file.readlines()
print("Length of the file: ", len(content))