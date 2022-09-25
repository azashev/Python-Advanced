def move(r, c):
    global presents, nice_kids_presents_count
    if matrix[r][c] == "V":
        nice_kids_presents_count += 1
        presents -= 1

    matrix[r][c] = "S"
    return [r, c]

def cookie(r, c):
    global presents, nice_kids_presents_count
    for current_direction, pos in directions.items():
        new_r = r + pos[0]
        new_c = c + pos[1]

        if matrix[new_r][new_c] == "V":
            nice_kids_presents_count += 1
            presents -= 1
        elif matrix[new_r][new_c] == "X":
            presents -= 1
        matrix[new_r][new_c] = "-"

presents = int(input())
size = int(input())

santa_symbol = "S"
nice_kids_symbol = "V"
matrix = []
santas_position = []
total_nice_kids = 0
nice_kids_presents_count = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    line = input().split()
    matrix.append(line)

    if santa_symbol in line:
        santas_position = ([row, line.index(santa_symbol)])
    if nice_kids_symbol in line:
        total_nice_kids += line.count(nice_kids_symbol)

while presents > 0:
    direction = input()
    if direction == "Christmas morning":
        break

    r = santas_position[0] + directions[direction][0]
    c = santas_position[1] + directions[direction][1]

    if 0 <= r < size and 0 <= c < size:
        matrix[santas_position[0]][santas_position[1]] = "-"
        if matrix[r][c] == "C":
            matrix[r][c] = "S"
            santas_position = cookie(r, c)
        else:
            santas_position = move(r, c)

if presents < 1 and nice_kids_presents_count < total_nice_kids:
    print("Santa ran out of presents!")

[print(*x) for x in matrix]

if nice_kids_presents_count == total_nice_kids:
    print(f"Good job, Santa! {nice_kids_presents_count} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_presents_count} nice kid/s.")
