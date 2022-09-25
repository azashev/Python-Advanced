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
