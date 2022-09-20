expression = input()

starting_indexes = []

for i in range(len(expression)):
    if expression[i] == '(':
        starting_indexes.append(i)
    elif expression[i] == ')':
        start_index = starting_indexes.pop()
        print(expression[start_index:i + 1])
