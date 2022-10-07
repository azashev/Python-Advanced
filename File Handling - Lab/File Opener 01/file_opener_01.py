try:
    file = open('text.txt')
    print("File found")
except FileNotFoundError:
    print("File not found")

# You are given a file called text.txt with the following text:
#
# This is some random line
# This is the second line
# And this is the third one
#
# Create a program that opens the file. If the file is found, print 'File found'.
# If the file is not found, print 'File not found'.
