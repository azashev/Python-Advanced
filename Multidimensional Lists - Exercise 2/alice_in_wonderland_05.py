size = int(input())

alice_symbol = "A"
matrix = []
starting_position = []
tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    line = input().split()
    matrix.append(line)
    if alice_symbol in line:
        starting_position = [row, line.index(alice_symbol)]
        matrix[row][starting_position[1]] = "*"

while tea_bags < 10:
    current_direction = input()

    current_row = starting_position[0] + directions[current_direction][0]
    current_col = starting_position[1] + directions[current_direction][1]

    if not (0 <= current_row < size and 0 <= current_col < size):
        break

    starting_position = [current_row, current_col]
    current_position = matrix[current_row][current_col]
    matrix[current_row][current_col] = "*"

    if current_position == "R":
        break

    if current_position.isdigit():
        tea_bags += int(current_position)

if not tea_bags >= 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*x) for x in matrix]
