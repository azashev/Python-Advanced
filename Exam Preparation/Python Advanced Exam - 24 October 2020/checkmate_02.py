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
