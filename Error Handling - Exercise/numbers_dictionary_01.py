# Solution

numbers_dictionary = {}

line = input()

while line != "Search":
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

    line = input()

line = input()
while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

line = input()
while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)



# Description:
#
# You are provided with the following code:
#
# numbers_dictionary = {}
#
# line = input()
#
# while line != "Search":
#     number_as_string = line
#     number = int(input())
#     numbers_dictionary[number_as_string] = number
#
# line = input()
#
# while line != "Remove":
#     searched = line
#     print(numbers_dictionary[searched])
#
# line = input()
#
# while line != "End":
#     searched = line
#     del numbers_dictionary[searched]
#
# print(numbers_dictionary)
#
#
# • On the first several lines, until you receive the command "Search", you will receive on separate lines the number as
# a text and the number as an integer
# • When you receive "Search" on the next several lines until you receive the command "Remove", you will be given the
# searched number as a text, and you need to print it on the console
# • When you receive "Remove" on the next several lines until you receive "End", you will be given the searched number
# as a text, and you need to remove it from the dictionary
# • In the end, you need to print what is left from the dictionary
#
# There is some missing code in the solution, and some errors may occur. Complete the code, so the following errors are
# handled:
# • Passing non-integer type to the variable number
# • Searching for a non-existent number
# • Removing a non-existent number
#
# Print appropriate messages when an error has occurred. The messages should be:
# •	"The variable number must be an integer"
# •	"Number does not exist in dictionary" - for non-existing keys
#
#
#
# Input 1:
# one
# 1
# two
# 2
# Search
# one
# Remove
# two
# End
#
# Output 1:
# 1
# {'one': 1}
#
#
#
# Input 2:
# one
# two
# Search
# Remove
# End
#
# Output 2:
# The variable number must be an integer
# {}
#
#
#
# Input 3:
# one
# 1
# Search
# one
# Remove
# two
# End
#
# Output 3:
# 1
# Number does not exist in dictionary
# {'one': 1}
