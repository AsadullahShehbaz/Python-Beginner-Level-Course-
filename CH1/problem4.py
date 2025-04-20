# To list the contents of a directory in Python, you can use the os module's listdir() function. This function returns a list of all files and directories in the specified path. 

# Here's a simple program to use os.listdir():


import os

# Define the path to the directory you want to list
directory_path = '/Semester 6/Web Engineering'

# Get a list of all items in the specified directory
content = os.listdir(directory_path)
print(content)
# Iterate over each item in the directory and print its name
# for item in content:


