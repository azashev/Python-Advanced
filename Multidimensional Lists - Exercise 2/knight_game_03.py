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
