import os
import shutil
 
# Path of the folder that you want to sort
path = 'C:\\Users\\your_name\\your_folder'

# Gets the files of the folder in a list
list = os.listdir(path)
 
# Loops through every file of the list
for file in list :
    # Gets the name and the extension of the file
    name, ext = os.path.splitext(file)

    # Gets the extension type of the file without the '.'
    ext = ext[1:]

    # If the element is a directory, do nothing
    if ext == '':
        continue

    # If a directory with the name already exists, then moves the file to that directory
    if os.path.exists(path + '/' + ext):
       shutil.move(path + '/' + file, path + '/' + ext + '/' + file)

    # If the directory does not exist, then creates a new directory
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)