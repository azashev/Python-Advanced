word = input()
size = int(input())

current_position = ()

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix = []

for r in range(size):
    row = list(input())
    if "P" in row:
        current_position = (r, row.index("P"))
        row[row.index("P")] = "-"
    matrix.append(row)

n = int(input())

for _ in range(n):
    command = input()

    if 0 <= current_position[0] + directions[command][0] < size and 0 <= current_position[1] + \
            directions[command][1] < size:
        current_position = (current_position[0] + directions[command][0], current_position[1] + directions[command][1])
        if matrix[current_position[0]][current_position[1]] != "-":
            word += matrix[current_position[0]][current_position[1]]
            matrix[current_position[0]][current_position[1]] = "-"
    else:
        if word:
            word = word[:-1]

matrix[current_position[0]][current_position[1]] = "P"
print(word)
[print(''.join(x)) for x in matrix]
