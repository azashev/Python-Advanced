from collections import deque

string_input = deque(input().split())

main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']

result = deque()

while string_input:
    if len(string_input) > 1:
        first_substring = string_input.popleft()
        last_substring = string_input.pop()
        substring_1 = first_substring + last_substring
        substring_2 = last_substring + first_substring

        if substring_1 in main_colors or substring_1 in secondary_colors:
            result.append(substring_1)
        elif substring_2 in main_colors or substring_2 in secondary_colors:
            result.append(substring_2)
        else:
            i = len(string_input) // 2
            first_substring = first_substring[:-1]
            last_substring = last_substring[:-1]
            if first_substring:
                string_input.insert(i, first_substring)
            if last_substring:
                string_input.insert(i, last_substring)
    else:
        substring = string_input.pop()
        if substring in main_colors or substring in secondary_colors:
            result.append(substring)

if 'orange' in result:
    if 'red' not in result or 'yellow' not in result:
        result = [x for x in result if not x == 'orange']

if 'purple' in result:
    if 'red' not in result or 'blue' not in result:
        result = [x for x in result if not x == 'purple']

if 'green' in result:
    if 'yellow' not in result or 'blue' not in result:
        result = [x for x in result if not x == 'green']

print(list(result))
