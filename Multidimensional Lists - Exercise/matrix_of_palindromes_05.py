rows, cols = [int(x) for x in input().split()]

matrix = []

start = 97

for row in range(rows):
    current_list = []
    for col in range(cols):
        current_list.append(chr(start + row) + chr(col + row + start) + chr(start + row))
    matrix.append(current_list)

[print(*x) for x in matrix]
