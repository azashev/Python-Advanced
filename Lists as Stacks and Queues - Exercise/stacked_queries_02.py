stack = []

n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == '1':
        number = int(command[1])
        stack.append(number)
    elif command[0] == '2' and stack:
        stack.pop()
    elif command[0] == '3' and stack:
        print(max(stack))
    elif command[0] == '4' and stack:
        print(min(stack))

while stack:
    num = stack.pop()
    if stack:
        print(num, end=', ')
    else:
        print(num)
