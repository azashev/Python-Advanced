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


# You will be given a string. Then, you will be given an integer N for the size of the field with square shape.
# On the next N lines, you will receive the rows of the field.
# The player will be placed on a random position, marked with "P".
# On random positions there will be letters. All of the empty positions will be marked with "-".
#
# Each turn you will be given commands for the player’s movement. If he moves to a letter, he consumes it, concatеnates
# it to the initial string and the letter disappears from the field. If he tries to move outside of the field, he is
# punished - he loses the last letter in the string, if there are any, and the player’s position is not changed.
#
# At the end print all letters and the field.
#
#
# Input:
# • On the first line, you are given the initial string
# • On the second line, you are given the integer N - the size of the square matrix
# • The next N lines holds the values for every row
# • On the next line you receive a number M
# • On the next M lines you will get a move command
#
# Output:
# • On the first line the final state of the string
# • In the end print the matrix
#
# Constraints:
# • The size of the square matrix will be between [2…10]
# • The player position will be marked with "P"
# • The letters on the field will be any letter except for "P"
# • Move commands will be: "up", "down", "left", "right"
#
#
#
# Input:
# Hello
# 4
# P---
# Mark
# -l-y
# --e-
# 4
# down
# right
# right
# right
#
# Expected output:
# HelloMark
# ----
# ---P
# -l-y
# --e-
#
#
#
# Input:
# Initial
# 5
# -----
# t-r--
# --Pa-
# --S--
# z--t-
# 4
# up
# left
# left
# left
#
# Expected output:
# Initialr
# -----
# P----
# ---a-
# --S--
# z--t-
