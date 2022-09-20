from collections import deque

string_expr = input().split()
numbers = deque()

for symbol in string_expr:
    if symbol in '*+-/':
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()

            if symbol == '+':
                numbers.appendleft(first_num + second_num)
            elif symbol == '-':
                numbers.appendleft(first_num - second_num)
            elif symbol == '*':
                numbers.appendleft(first_num * second_num)
            elif symbol == '/':
                numbers.appendleft(first_num // second_num)
    else:
        numbers.append(int(symbol))

print(*numbers)
