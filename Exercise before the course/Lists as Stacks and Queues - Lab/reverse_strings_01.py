# Write program that:
# • Reads an input string
# • Reverses it using a stack
# • Prints the result back on the console

input_string = list(input())

while input_string:
    print(input_string.pop(), end='')
