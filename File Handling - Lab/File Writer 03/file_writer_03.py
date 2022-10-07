# Create a program that creates a file called my_first_file.txt.
# In that file, write a single line with the content: 'I just created my first file!'

with open('my_first_file.txt', 'w') as file:
    file.write('I just created my first file!')
