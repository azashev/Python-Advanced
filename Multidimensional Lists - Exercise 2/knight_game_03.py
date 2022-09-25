rows = int(input())

matrix = [[x for x in list(input())] for _ in range(rows)]

knights = 0
removed_knights = 0

positions = (
    (-2, -1),
    (-1, -2),
    (-2, 1),
    (-1, 2),
    (2, -1),
    (1, -2),
    (2, 1),
    (1, 2)
)

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(rows):
        for col in range(rows):
            if matrix[row][col] == "K":
                knight_attacks = 0

                for position in positions:
                    r = position[0] + row
                    c = position[1] + col
                    if 0 <= r < rows and 0 <= c < rows:
                        if matrix[r][c] == "K":
                            knight_attacks += 1
                if knight_attacks > max_attacks:
                    max_attacks = knight_attacks
                    knight_with_most_attacks_pos = [row, col]

    if knight_with_most_attacks_pos:
        matrix[knight_with_most_attacks_pos[0]][knight_with_most_attacks_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)


# Chess is the oldest game, but it is still popular these days.
# It will be used only one chess piece for this task - the Knight.
#
# A chess knight has 8 possible moves it can make. It can move to the nearest square but not on the same row, column, or
# diagonal. (e.g., it can move two squares horizontally, then one square vertically, or it can move one square
# horizontally then two squares vertically - i.e., in an "L" pattern.)
#
# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells.
#
# Your task is to remove knights until no knights that can attack one another with one move are left.
# Always remove the knight who can attack the greatest number of knights.
#
# If there are two or more knights with the same number of attacks, remove the top-left one.
#
#
# Input:
# • On the first line, you will receive integer N - the size of the board
# • On the following N lines, you will receive strings with "K" and "0"
#
# Output:
# • Print a single integer with the number of knights that need to be removed.
#
#
# Constraints:
# • The size of the board will be 0 < N < 30
# • Time limit: 0.3 sec. Memory limit: 16 MB

#
# Input
# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0

# Output:
# 1


# Input:
# 2
# KK
# KK

# Output:
# 0


# Input:
# 8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK

# Output:
# 12
