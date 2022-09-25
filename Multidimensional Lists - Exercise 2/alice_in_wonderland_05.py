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


# Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
#
# You will be given an integer n for the size of the Wonderland territory with a square shape.
#
# On the following n lines, you will receive the rows of the territory:
# • Alice will be placed in a random position, marked with the letter "A".
# • On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, she
# collects the tea bags and increases the quantity with the corresponding number.
# • There will always be one rabbit hole on the territory marked with the letter "R"
# • All of the empty positions will be marked with "."
#
#
# After the field state, you will be given commands for Alice's movements.
# Move commands can be: "up", "down", "left" or "right".
#
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue
# collecting.
# Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.
#
# In the end, the path she walked had to be marked with '*'.
#
#
# Input:
# • On the first line, you will be given the integer n – the size of the square matrix
# • On the following n lines - matrix representing the field (each position separated by a single space)
# • On each of the following lines, you will be given a move command
#
# Output:
# • On the first line:
#   - If Alice steps on the rabbit hole or she go out of the territory, print:
#       "Alice didn't make it to the tea party."
#   - If she collected at least 10 bags of tea, print:
#       "She did it! She went to the party."
#
# •	On the following lines, print the matrix.
#
#
# Constraints:
# • Alice will always either go outside the Wonderland or collect 10 bags of tea
# • All the commands will be valid
# • All of the given numbers will be valid integers in the range [0, 10]


#
# Input:
# 5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left

# Output:
# Alice didn't make it to the tea party.
# . * . . 1
# * * * . .
# 4 * . 1 .
# . . . 2 .
# . 3 . . .


# Input:
# 7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right

# Output:
# She did it! She went to the party.
# * * . 1 1 . .
# * . . . 6 . 5
# * * . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
