n = int(input())

stack = []

for _ in range(n):
    query = input().split()

    if query[0] == '1':
        number = int(query[1])
        stack.append(number)
    elif query[0] == '2' and stack:
            stack.pop()
    elif query[0] == '3' and stack:
            print(max(stack))
    elif query[0] == '4' and stack:
            print(min(stack))

while stack:
    element = stack.pop()
    if len(stack):
        print(element, end=', ')
    else:
        print(element)


# You have an empty stack. You will receive an integer – N.
# On the next N lines, you will receive queries.
# Each query is one of these four types:
# • '1 {number}' - push the number (integer) into the stack
# • '2' - delete the number at the top of the stack
# • '3' - print the maximum number in the stack
# • '4' - print the minimum number in the stack
#
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from top to bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"
