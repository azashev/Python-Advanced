matrix = []
king_positions = ()
queens_positions = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "upperleft": (-1, -1),
    "upperright": (-1, 1),
    "lowerleft": (1, -1),
    "lowerright": (1, 1)
}

for row in range(8):
    line = input().split()

    if "K" in line:
        king_positions = (row, line.index("K"))
    matrix.append(line)

for row in range(8):
    for col in range(8):
        if matrix[row][col] == "Q":
            captured_the_king = False
            for direction, values in directions.items():
                if captured_the_king:
                    break
                r = row + values[0]
                c = col + values[1]
                while 0 <= r < 8 and 0 <= c < 8:
                    if matrix[r][c] == "Q":
                        break
                    elif matrix[r][c] == "K":
                        queens_positions.append([row, col])
                        captured_the_king = True
                        break
                    r += values[0]
                    c += values[1]

if queens_positions:
    [print(x) for x in queens_positions]
else:
    print("The king is safe!")


# You will be given a chess board (8x8). On the board there will be 3 types of symbols:
# • "." - empty square
# • "Q" - a queen
# • "K" - the king
#
# Your job is to find which queens can capture the king and print them.
# The moves that the queen can do is to move diagonally, horizontally and vertically (basically all the moves that all
# the other figures can do except from the knight).
#
# Beware that there might be queens that stand in the way of other queens and can stop them from capturing the king.
# For more clarification see the examples.
#
# Input:
# • 8 lines - the state of the board (each square separated by single space)
#
# Output:
# • The positions of the queens that can capture the king as lists
# • If the king cannot be captured, print: "The king is safe!"
# • The order of output does not matter
#
# Constrains:
# • There will always be exactly 8 lines
# • There will always be exactly one King
# • Only the 3 symbols described above will be present in the input
#
#
#
# Input:
# . . . . . . . .
# Q . . . . . . .
# . K . . . Q . .
# . . . Q . . . .
# Q . . . Q . . .
# . Q . . . . . .
# . . . . . . Q .
# . Q . Q . . . .
#
# Expected output:
# [2, 5]
# [5, 1]
# [1, 0]
#
#
#
# Input:
# . . . . . . . .
# . . . Q . . . .
# . . . . . . . .
# . . . . . . . .
# Q . . . Q . . .
# . . K . . . . .
# . . . . . . Q .
# . . . Q . . . .
#
# Expected output:
# The king is safe!
