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


# You will receive a 6x6 field on separate lines with:
# • One rover - marked with the letter "E"
# • Water deposit (one or many) - marked with the letter "W"
# • Metal deposit (one or many) - marked with the letter "M"
# • Concrete deposit (one or many) - marked with the letter "C"
# • Rock (one or many) - marked with the letter "R"
# • Empty positions will be marked with "-"
#
# After that, you will be given the commands for the rover's movement on one line separated by a comma and a
# space (", ").
# Commands can be: "up", "down", "left", or "right".
#
# For each command, the rover moves in the given directions with one step, and it can land on one of the given types of
# deposit or a rock:
# • When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and increase
#   its value by 1.
# • If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown below,
#   and the program ends.
# • If the rover goes out of the field, it should continue from the opposite side in the same direction.
#
# Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be placed at
# position (3, 5).
#
# The rover needs to find at least one of each deposit to consider the area suitable to start our colony.
#
# Stop the program if you run out of commands or the rover gets broken.
#
#
# Input:
# • On the first 6 lines, you will receive the matrix.
# • On the following line, you will receive the commands for the rover separated by a comma and a space.
#
# Output:
# • For each deposit found while you go through the commands, print out on the console:
#   "{Water, Metal or Concrete} deposit found at ({row}, {col})"
# • If the rover hits a rock, print the coordinates where it got broken in the format:
#   "Rover got broken at ({row}, {col})"
#
# After you go through all the commands or the rover gets broken, print out on the console:
# • If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
# • Otherwise, print on the console: "Area not suitable to start the colony."
#
#
#
# Tests:
#
# Input:
# - R - - - -
# - - - - - R
# - E - R - -
# - W - - - -
# - - - C - -
# M - - - - -
# down, right, down, right, down, left, left, left
#
# Expected output:
# Water deposit found at (3, 1)
# Concrete deposit found at (4, 3)
# Metal deposit found at (5, 0)
# Area suitable to start the colony.
#
#
#
# Input:
# R - - - - -
# - - C - - -
# - - - - M -
# - - W - - -
# - E - W - R
# - - - - - -
# up, right, down, right, right, right
#
# Expected output:
# Water deposit found at (3, 2)
# Water deposit found at (4, 3)
# Rover got broken at (4, 5)
# Area not suitable to start the colony.
#
#
#
# Input:
# R - - - - -
# - - C - - -
# - - - - M -
# C - M - R M
# - E - W - -
# - - - - - -
# right, right, up, left, left, left, left, left
#
# Expected output:
# Water deposit found at (4, 3)
# Metal deposit found at (3, 2)
# Concrete deposit found at (3, 0)
# Metal deposit found at (3, 5)
# Rover got broken at (3, 4)
# Area suitable to start the colony.
