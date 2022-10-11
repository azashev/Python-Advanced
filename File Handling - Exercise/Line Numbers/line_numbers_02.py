from string import punctuation

output_file = open("./output.txt", "a")

with open("./text.txt", "r") as text_file:
    text = text_file.readlines()

for i in range(len(text)):
    row = text[i]

    letters = 0
    marks = 0

    for symbol in row:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {i+1}: {''.join(row[:-1])} ({letters})({marks})\n")

output_file.close()


# Write a program that reads a text file, inserts line numbers in front of each line, and counts all the letters and
# punctuation marks. The result should be written to another text file.
#
#
#
# Output:
# Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)
# Line 2: -Is this some kind of joke?! Is it? (24)(4)
# Line 3: -Quick, hide here. It is safer. (22)(4)
