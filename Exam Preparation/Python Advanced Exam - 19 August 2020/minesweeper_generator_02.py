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


# You will be given an integer n for the size of the mines field with square shape and another one for the number of
# bombs that you have to place in the field.
# On the next n lines, you will receive the position for each bomb.
# Your task is to create the game field placing the bombs at the correct positions and mark them with "*", and calculate
# the numbers in each cell of the field. Each cell represents a number of all bombs directly near it:
# up, down, left, right and the 4 diagonals
#
#
# Input:
# • On the first line, you are given the integer n – the size of the square matrix.
# • On the second line – the number of the bombs.
# • The next n lines holds the position of each bomb.
#
# Output:
# • Print the matrix you've created.
#
# Constraints:
# • The size of the square matrix will be between [2…15].
#
#
#
# Input:
# 4
# 4
# (0, 3)
# (1, 1)
# (2, 2)
# (3, 0)
#
# Expected output:
# 1 1 2 *
# 1 * 3 2
# 2 3 * 1
# * 2 1 1
#
#
#
# Input:
# 5
# 3
# (1, 1)
# (2, 4)
# (4, 1)
#
# Expected output:
# 1 1 1 0 0
# 1 * 1 1 1
# 1 1 1 1 *
# 1 1 1 1 1
# 1 * 1 0 0
