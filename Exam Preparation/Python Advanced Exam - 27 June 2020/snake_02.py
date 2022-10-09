size = int(input())

snake_current_position = []
burrow = []
matrix = []
food = 0

positions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    line = list(input())
    matrix.append(line)
    if "S" in line:
        snake_current_position = [row, line.index("S")]
        matrix[row][line.index("S")] = "."
    if "B" in line:
        burrow.append([row, line.index("B")])


while food < 10:
    direction = input()
    r = snake_current_position[0] + positions[direction][0]
    c = snake_current_position[1] + positions[direction][1]

    if not 0 <= r < size or not 0 <= c < size:
        matrix[snake_current_position[0]][snake_current_position[1]] = "."
        print("Game over!")
        break

    matrix[snake_current_position[0]][snake_current_position[1]] = "."

    if matrix[r][c] == "B":
        matrix[r][c] = "."
        burrow.remove([r, c])
        current_burrow_row = burrow[0][0]
        current_burrow_col = burrow[0][1]

        snake_current_position = [current_burrow_row, current_burrow_col]
        matrix[current_burrow_row][current_burrow_col] = "S"
        continue
    elif matrix[r][c] == "*":
        food += 1
        matrix[r][c] = "S"
        snake_current_position = [r, c]
        continue
    matrix[r][c] = "S"
    snake_current_position = [r, c]

if food > 9:
    print("You won! You fed the snake.")

print(f"Food eaten: {food}")
[print(''.join(x)) for x in matrix]


# You will be given an integer n for the size of the snake territory with square shape.
# On the next n lines, you will receive the rows of the territory.
# The snake will be placed on a random position, marked with the letter 'S'.
# On random positions there will be food, marked with '*'.
# There might also be a lair on the territory. The lair has two burrows. They are marked with the letter - 'B'.
# All of the empty positions will be marked with '-'.
#
# Each turn, you will be given command for the snake’s movement. When the snake moves it leaves a trail marked with '.'
# Move commands will be: "up", "down", "left", "right".
#
# If the snake moves to a food, it eats the food and increases the food quantity with one.
# If it goes inside of a burrow, it goes out on the position of the other burrow and then both burrows disappear.
# If the snake goes out of its territory, it loses, can't return back and the program ends.
#
# The snake needs at least 10 food quantity to win.
# When the snake has gone outside of its territory or has eaten enough food, the game ends.
#
#
# Input:
# • On the first line, you are given the integer n – the size of the square matrix.
# • The next n lines holds the values for every row.
# • On each of the next lines you will get a move command.
#
# Output:
# • On the first line:
#   - If the snake goes out of its territory, print: "Game over!"
#   - If the snake eat enough food, print: "You won! You fed the snake."
# • On the second line print all food eaten: "Food eaten: {food quantity}"
# • In the end print the matrix.
#
#
# Constraints:
# • The size of the square matrix will be between [2...10].
#• There will always be 0 or 2 burrows, marked with - 'B'.
# • The snake position will be marked with 'S'.
# • The snake will always either go outside its territory or eat enough food.
# • There will be no case in which the snake will go through itself.
