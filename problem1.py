# Here’s a simple Python program that prints the contents of a directory using the built-in os module

import os

# Path of the directory
directory_path = "/Users"

try:
    # List all files and folders in the directory
    contents = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Directory not found.")
except PermissionError:
    print("Permission denied.")
