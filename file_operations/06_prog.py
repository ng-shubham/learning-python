# Program: Check If File Exists
import os

if os.path.exists("file_operations/myfile.txt"):
    print("File exist!")
else:
    print("File not exist!")