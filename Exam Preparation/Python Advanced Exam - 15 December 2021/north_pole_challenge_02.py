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
