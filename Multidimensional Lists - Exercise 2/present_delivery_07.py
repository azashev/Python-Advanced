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


# The presents are ready, and Santa has to deliver them to the kids.
#
# You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood
# with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood.
# Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live.
# If the cell has "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is
# marked by "V".
# There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".
#
# Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you receive.
#
#
# If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty kid,
# he doesn't drop a present.
# If the command sends Santa to a cell marked with "C", Santa eats cookies and becomes happy and extra generous to all
# the kids around him* (meaning all of them will receive presents - it doesn't matter if naughty or nice).
# If Santa has been to a house, the cell becomes "-".
#
# Note: *around him means on his left, right, upwards, and downwards by one cell.
# In this case, Santa doesn't move to these cells, or if he does, he returns to the cell where the cookie was.
#
#
# If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
# Keep in mind that you should check whether all the nice kids received presents.
#
#
# Input:
# • On the first line, you are given the integer m - the count of presents
# • On the second - integer n - the size of the neighborhood
# • The following n lines hold the values for every row
# • On each of the following lines you will get a command
#
# Output:
# • On the first line:
#   - If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"
# • Next, print the matrix.
# • In the end, print one of these messages:
#   - If he manages to give all the nice kids presents, print:
#       "Good job, Santa! {count_nice_kids} happy nice kid/s."
#   - Otherwise, print:
#       "No presents for {count nice kids} nice kid/s."
#
#
# Constraints:
# • The size of the square matrix will be between [2…10].
# • Santa's position will be marked with 'S'.
# • There will always be at least 1 nice kid.
# • There won't be a case where the cookie is on the border of the matrix.


# Input
# 5
# 4
# - X V -
# - S - V
# - - - -
# X - - -
# up
# right
# down
# right
# Christmas morning

# Output:
# - - - -
# - - - S
# - - - -
# X - - -
# Good job, Santa! 2 happy nice kid/s.


# Input:
# 3
# 4
# - - - -
# V - X -
# - V C V
# - - - S
# left
# up

# Output:
# Santa ran out of presents!
# - - - -
# V - - -
# - - S -
# - - - -
# No presents for 1 nice kid/s.
