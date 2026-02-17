#Program: Append Data to File

with open("file_operations/myfile.txt", 'a') as file:
    file.write("\n This is new line 2")

print("Data appended successfully.")