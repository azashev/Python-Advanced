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


# Your task is to collect as many eggs as possible.
#
# On the first line, you will be given a number representing the size of the field.
#
# On the following few lines, you will be given a field with:
# • One bunny - randomly placed in it and marked with the symbol "B"
# • Number of eggs placed at different positions of the field and traps marked with "X"
#
#
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# The directions that should be considered as possible are up, down, left, and right.
#
# If you reach a trap while checking some of the directions, you should not consider the fields after the trap in
# this direction.
#
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
#
#
# Input:
# • A number representing the size of the field
# • The matrix representing the field (each position separated by a single space)
#
# Output:
# • The direction which should be considered as best (lowercase)
# • The field positions from which we are collecting eggs as lists
# • The total number of eggs collected
#
#
# Constraints:
# • There will NOT be two or more paths consisting of the same total amount of eggs


#
# Input
# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0

# Output:
# right
# [3, 1]
# [3, 2]
# [3, 3]
# [3, 4]
# 87


# Input:
# 8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22

# Output:
# down
# [6, 2]
# [7, 2]
# 113
