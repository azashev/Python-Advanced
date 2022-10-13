size = int(input())
bombs = int(input())

matrix = [[0 for x in range(size)] for x in range(size)]

directions = {
    "up": (1, 0),
    "down": (-1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "upperleft": (-1, -1),
    "upperright": (-1, 1),
    "lowerleft": (1, -1),
    "lowerright": (1, 1)
}

for _ in range(bombs):
    r, c = eval(input())
    matrix[r][c] = "*"

    for direction, value in directions.items():
        row = r + value[0]
        col = c + value[1]

        if 0 <= row < size and 0 <= col < size:
            if matrix[row][col] != "*":
                matrix[row][col] += 1

[print(*x) for x in matrix]
