# You are given an algebraic expression with parentheses.
# Scan through the string and extract each set of parentheses.
# Print the result back on the console.


input_string = input()

stack_indexes = []

for index in range(len(input_string)):
    if input_string[index] == "(":
        stack_indexes.append(index)
    elif input_string[index] == ")":
        start_index = stack_indexes.pop()
        print(input_string[start_index:index + 1])
