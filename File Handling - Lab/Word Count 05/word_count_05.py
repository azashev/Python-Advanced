import re

list_of_words = []
result = {}

with open('words.txt', 'r') as words:
    list_of_words = words.read().split()
    result = {x.lower(): 0 for x in list_of_words}

with open('input.txt', 'r') as text:
    for word in text:
        line = re.findall('[A-z\']+', word)
        for x in line:
            current_word = x.lower()
            if current_word in result:
                result[current_word] += 1

with open('output.txt', 'w') as result_file:
    sorted_result = sorted(result.items(), key=lambda x: -x[1])
    for word, count in sorted_result:
        result_file.write(f"{word} - {count}\n")





# Write a program that reads a list of words from the file words.txt and finds how many times each of the words is
# contained in another file input.txt. Matching should be case-insensitive.
# The results should be written to other text files. Sort the words by frequency in descending order.
#
#
# Examples:
#
#   words.txt:	                           input.txt:	                                    output.txt:
# quick is fault          -I was quick to judge him, but it wasn't his fault.                 is - 3
#                         -Is this some kind of joke?! Is it?                                 quick - 2
#                         -Quick, hide here…It is safer.                                      fault - 1
#
#
