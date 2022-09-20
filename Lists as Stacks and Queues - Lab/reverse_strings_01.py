input_string = list(input())
stack = []

while input_string:
    stack.append(input_string.pop())

print("".join(stack))
