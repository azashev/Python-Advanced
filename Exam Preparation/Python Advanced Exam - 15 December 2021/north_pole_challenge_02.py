def action(matrix, row, col, direction, steps):
    items = {}
    for _ in range(steps):
        оld_row = row
        old_col = col
        matrix[row][col] = 'x'
        row, col = dir1(matrix, row, col, direction)

        if matrix[row][col] == 'D':
            if 'Christmas decorations' not in items:
                items['Christmas decorations'] = 0
            items['Christmas decorations'] += 1
            matrix[row][col] = 'Y'
        elif matrix[row][col] == 'G':
            if 'Gifts' not in items:
                items['Gifts'] = 0
            items['Gifts'] += 1
            matrix[row][col] = 'Y'
        elif matrix[row][col] == 'C':
            if 'Cookies' not in items:
                items['Cookies'] = 0
            items['Cookies'] += 1
            matrix[row][col] = 'Y'
        matrix[row][col] = 'Y'
        for r in matrix:
            if 'D' in r or 'G' in r or 'C' in r:
                break
        else:
            return matrix, [row, col], items, True

    return matrix, [row, col], items, False


def dir1(m, r, c, direction):
    if direction == 'up':
        r -= 1
        if r < 0:
            r = len(m) - 1
        return r, c
    elif direction == 'down':
        r += 1
        if r >= len(m):
            r = 0
        return r, c
    elif direction == 'left':
        c -= 1
        if c < 0:
            c = len(m[0]) - 1
        return r, c
    elif direction == 'right':
        c += 1
        if c >= len(m[0]):
            c = 0
        return r, c

    return r, c


rows, cols = [int(x) for x in input().split(', ')]
workshop = []
coords = []

for row in range(rows):
    line = input().split()
    if "Y" in line:
        coords = [row, line.index("Y")]
    workshop.append(line)

collected_items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0
}

merry_christmas = False

while True:
    if merry_christmas:
        break

    command = input()
    if command == "End":
        break

    direction, steps = command.split('-')
    steps = int(steps)

    workshop, coords, new_items, merry_christmas = action(workshop, coords[0], coords[1], direction, steps)
    if new_items:
        for item, quantity in new_items.items():
            collected_items[item] += quantity

if merry_christmas:
    print("Merry Christmas!")

print("You've collected:")
for item, quantity in collected_items.items():
    print(f"- {quantity} {item}")

[print(*x) for x in workshop]


# You will be given the size of the matrix in the format "{rows}, {columns}".
# It is the Santa's workshop represented as some symbols separated by a single space:
# • Your position is marked with the symbol "Y"
# • Christmas decorations are marked with the symbol "D"
# • Gifts are marked with the symbol "G"
# • Cookies are marked with the symbol "C"
# • All of the empty positions will be marked with "."
#
# After the field state, you will be given commands until you receive the command "End".
# The commands will be in the format "right/left/up/down-{steps}"
#
# You should move in the given direction with the given steps and collect all the items that come across.
# If you go out of the field, you should continue to traverse the field from the opposite side in the same direction.
# You should mark your path with "x". Your current position should always be marked with "Y".
#
# Keep track of all collected items. If you've collected all items at any point, end the program and print:
#   "Merry Christmas!".
#
#
# Input:
# • On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
# • On the next lines, you will receive each row with its columns - symbols, separated by a single space.
# • On the following lines, you will receive commands in the format described above until you receive the command "End"
#   or until you collect all items.
#
# Output:
# • On the first line, if you have collected all items, print:
#   - "Merry Christmas!"
#   - Otherwise, skip the line
# • Next, print the number of collected items in the format:
#   - "You've collected:
#   - {number_of_decoration} Christmas decorations
#   - {number_of_gifts} Gifts
#   - {number_of_cookies} Cookies"
# • Finally, print the field, as shown in the examples.
#
# Constrains:
# • All the commands will be valid
# • There will always be at least one item
# • The dimensions of the matrix will be integers in the range [1, 20]
# • The field will always have only one "Y"
# • On the field, there will always be only the symbols shown above.
#
#
#
# Input:
# 6, 5
# . . . . .
# C . . G .
# . C . . .
# G . . C .
# . D . . D
# Y . . . G
# left-3
# up-1
# left-2
# right-7
# up-1
# End
#
# Expected output:
# You've collected:
# - 2 Christmas decorations
# - 1 Gifts
# - 0 Cookies
# . . . . .
# C . . G .
# . C . . .
# G . Y C .
# x x x x x
# x . x x x
#
#
#
# Input:
# 5, 6
# . . . . . .
# . . . . . .
# Y C D D . .
# . . . C . .
# . . . C . .
# right-3
# down-3
#
# Expected output:
# Merry Christmas!
# You've collected:
# - 2 Christmas decorations
# - 0 Gifts
# - 3 Cookies
# . . . . . .
# . . . . . .
# x x x x . .
# . . . x . .
# . . . Y . .
#
#
#
# Input:
# 5, 2
# . .
# . .
# . Y
# . .
# . G
# up-1
# left-11
# down-10
# End
#
# Expected output:
# You've collected:
# - 0 Christmas decorations
# - 0 Gifts
# - 0 Cookies
# x .
# Y x
# x x
# x .
# x G
