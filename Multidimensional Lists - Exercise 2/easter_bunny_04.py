size = int(input())

matrix = []

bunny_symbol = "B"
total_eggs = 0
best_field_positions = []
best_direction = None

starting_position = []

positions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    line = input().split()
    if "B" in line:
        starting_position = [row, line.index("B")]
    matrix.append(line)

for direction, position in positions.items():
    collected_eggs = 0
    path = []

    r, c = [
        starting_position[0] + position[0],
        starting_position[1] + position[1],
    ]

    while 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "X":
            break

        collected_eggs += int(matrix[r][c])
        path.append([r, c])
        r += position[0]
        c += position[1]

    if collected_eggs >= total_eggs:
        total_eggs = collected_eggs
        best_field_positions = path
        best_direction = direction

print(best_direction)
print(*best_field_positions, sep='\n')
print(total_eggs)
