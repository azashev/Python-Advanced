def move(direction, steps):
    r = starting_position[0] + (directions[direction][0] * step)
    c = starting_position[1] + (directions[direction][1] * step)

    if not 0 <= r < size or not 0 <= c < size or not matrix[r][c] == ".":
        return starting_position
    return [r, c]

def shoot(r,c , direction):
    shot_targets = 0
    while 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            shot_targets += 1
            indexes_of_shot_targets.append([r, c])
            break
        r += directions[direction][0]
        c += directions[direction][1]
    return shot_targets

size = 5

matrix = []
symbol = 'A'
starting_position = []
indexes_of_shot_targets = []
total_targets = 0
shot_targets = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    line = input().split()
    matrix.append(line)
    if symbol in line:
        starting_position = [row, line.index(symbol)]
        matrix[row][starting_position[1]] = "."
    if "x" in line:
        total_targets += line.count("x")

n = int(input())

for _ in range(n):
    if total_targets <= shot_targets:
        break

    input_line = input().split()
    command = input_line[0]

    if command == "move":
        move_direction = input_line[1]
        step = int(input_line[2])
        starting_position = move(move_direction, step)

    elif command == "shoot":
         shoot_direction = input_line[1]
         r = starting_position[0] + directions[shoot_direction][0]
         c = starting_position[1] + directions[shoot_direction][1]
         shot_targets += shoot(r, c, shoot_direction)

if total_targets > shot_targets:
    print(f"Training not completed! {total_targets - shot_targets} targets left.")
else:
    print(f"Training completed! All {total_targets} targets hit.")
print(*indexes_of_shot_targets, sep='\n')


# You are participating in a Firearm course. It is a training day at the shooting range.
#
# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a
# single space:
# • Your position is marked with the symbol "A"
# • Targets marked with symbol "x"
# • All of the empty positions will be marked with "."
#
# After the field state, you will be given an integer representing the number of commands you will receive.
#
# The possible commands are:
# • "move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move
# if the field you want to step on is marked with ".".
#
# • "shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
# Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot
# only the nearest target. When you have shot a target, the field becomes empty position (".").
#
# Validate the positions since they can be outside the field.
#
#
# Keep track of all the shot targets:
# • If at any point there are no targets left, end the program and print:
# "Training completed! All {count_targets} targets hit."
#
# • If, after you perform all the commands, there are some targets left print:
# "Training not completed! {count_left_targets} targets left."
#
# Finally, print the index positions of the targets that you hit, as shown in the examples.
#
#
# Input:
# • 5 lines representing the field (symbols, separated by a single space)
# • N - count of commands
# • On the following N lines - the commands in the format described above
#
# Output:
# • On the first line, print one of the following:
#   - If all the targets were shot
#       "Training completed! All {count_targets} targets hit."
#
#   - Otherwise:
#       "Training not completed! {count_left_targets} targets left."
#
# • Finally, print the index positions "[{row}, {column}]" of the targets that you hit.
#
#
# Constrains:
# • All the commands will be valid
# • There will always be at least one target
