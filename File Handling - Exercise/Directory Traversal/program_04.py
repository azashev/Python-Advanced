from os import listdir, path

def traverse_dir(current_path, files_extensions):
    for file in listdir(current_path):
        if path.isdir(path.join(current_path, file)):
            traverse_dir(path.join(current_path, file), files_extensions)
        else:
            extension = file.split('.')[-1]
            if extension not in files_extensions:
                files_extensions[extension] = []
            files_extensions[extension].append(file)


file_extensions = {}
traverse_dir('.', file_extensions)

for extension, files in sorted(file_extensions.items(), key=lambda x: x[0]):
    report = open('report.txt', 'a')
    report.write(f'.{extension}\n')
    for file in sorted(files):
        report.write(f'--- {file}\n')
    report.close()


# Write a program that traverses a given directory for all files. Search through the first level of the directory only
# and write information about each found file in report.txt. The files should be grouped by their extension.
# Extensions should be ordered by name alphabetically.
# The files with extensions should also be sorted by name. report.txt should be saved in the chosen directory.
#
#
#
# Input:
# No input - the program will list from the current directory ./
#
#
# Directory view:
# /example
#   index.html
#   index.js
#   python.py
# demo.pptx
# log.txt
# notes.txt
# program.py
#
#
# Output:
# in report.txt
