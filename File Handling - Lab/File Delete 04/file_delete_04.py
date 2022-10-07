# Create a program that deletes the file you created in the previous task.
# If you try to delete the file multiple times, print the message: 'File already deleted!'.

from os import remove

try:
    remove('../File Writer 03/my_first_file.txt')

except FileNotFoundError:
    print("File already deleted!")
