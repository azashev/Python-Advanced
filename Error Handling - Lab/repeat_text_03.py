try:
    text = input()
    times = int(input())
    print(text * times)
except ValueError as error:
    print("Variable times must be an integer")


# Write a program that receives a text on the first line and times (to repeat the text) that must be an integer.
# If the user passes a non-integer type for the times variable, handle the exception and print a message
# "Variable times must be an integer".
#
#
# Examples:
#
# Input                     Output
# Hello
# Bye	        Variable times must be an integer
#
#
# Hello
# 2	                      HelloHello
