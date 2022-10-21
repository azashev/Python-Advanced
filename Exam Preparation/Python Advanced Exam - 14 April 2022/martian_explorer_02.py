def move(row, col, direction):
    if direction == "up":
        row -= 1
        if row < 0:
            row = size - 1
    elif direction == "down":
        row += 1
        if row >= size:
            row = 0
    elif direction == "left":
        col -= 1
        if col < 0:
            col = size - 1
    elif direction == "right":
        col += 1
        if col >= size:
            col = 0

    return [row, col]


def is_suitable(materials):
    for deposit, amount in deposits.items():
        if amount == 0:
            return False
    return True


size = 6
field = []
rover_position = []
deposits = {
    "Water deposit": 0,
    "Metal deposit": 0,
    "Concrete deposit": 0
}

for row in range(size):
    line = input().split()
    if "E" in line:
        rover_position = [row, line.index("E")]
        line[line.index("E")] = "-"
    field.append(line)

commands = input().split(', ')[::-1]

while commands:
    command = commands.pop()
    rover_position = move(rover_position[0], rover_position[1], command)
    r, c = rover_position[0], rover_position[1]

    deposit = ''

    if field[r][c] == "W":
        deposits["Water deposit"] += 1
        deposit = "Water deposit"
    elif field[r][c] == "M":
        deposits["Metal deposit"] += 1
        deposit = "Metal deposit"
    elif field[r][c] == "C":
        deposits["Concrete deposit"] += 1
        deposit = "Concrete deposit"
    elif field[r][c] == "R":
        print(f"Rover got broken at ({r}, {c})")
        break

    if deposit != '':
        print(f"{deposit} found at ({r}, {c})")

if is_suitable(deposits):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
