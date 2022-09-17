balanced_parentheses = '(){}[]'

input_line = input()

opening_parentheses = []
are_balanced = True

for char in input_line:
    if char in '({[':
        opening_parentheses.append(char)
    elif not opening_parentheses:
        are_balanced = False
        break
    else:
        current_parentheses = opening_parentheses.pop()
        if current_parentheses + char not in balanced_parentheses:
            are_balanced = False
            break

if are_balanced and not opening_parentheses:
    print('YES')
else:
    print('NO')
