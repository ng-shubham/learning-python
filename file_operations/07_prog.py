 # Program: Rename a File
import os

folder_path = "TestFolder/log2"
old_path = os.path.join(folder_path, "test.txt")
new_path = os.path.join(folder_path, "test22.txt")

os.rename(old_path, new_path)   
