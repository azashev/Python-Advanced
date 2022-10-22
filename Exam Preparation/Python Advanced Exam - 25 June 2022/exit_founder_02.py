def player_move(row, col):
    if maze_field[row][col] == "E":
        return False, True, False
    elif maze_field[row][col] == "T":
        return False, False, True
    elif maze_field[row][col] == "W":
        return True, False, False

    return False, False, False

size = 6

player_one, player_two = input().split(', ')
maze_field = [[x for x in input().split()] for x in range(size)]
counter = 9
player_one_skips = False
player_two_skips = False

while True:
    position = input()
    row, col = int(position[1]), int(position[4])
    found_the_exit = False
    found_a_trap = False
    hit_a_wall = False

    if counter % 2 != 0:
        if player_one_skips:
            player_one_skips = False
            counter += 1
            continue
        counter += 1
        hit_a_wall, found_the_exit, found_a_trap = player_move(row, col)
        if hit_a_wall:
            print(f"{player_one} hits a wall and needs to rest.")
            player_one_skips = True
            continue
        elif found_a_trap:
            print(f"{player_one} is out of the game! The winner is {player_two}.")
            break
        elif found_the_exit:
            print(f"{player_one} found the Exit and wins the game!")
            break


    elif counter % 2 == 0:
        if player_two_skips:
            player_two_skips = False
            counter += 1
            continue
        counter += 1
        hit_a_wall, found_the_exit, found_a_trap = player_move(row, col)
        if hit_a_wall:
            print(f"{player_two} hits a wall and needs to rest.")
            player_two_skips = True
            continue
        elif found_a_trap:
            print(f"{player_two} is out of the game! The winner is {player_one}.")
            break
        elif found_the_exit:
            print(f"{player_two} found the Exit and wins the game!")
            break


# First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ".
# The order in which they are received determines the order in which they will take turns.
# The first player starts first.
#
# Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
# • Only one Exit - marked with the "E" letter
# • Trap (one, many, or none) - marked with the "T" letter
# • Wall (one, many, or none) - marked with the "W" letter
# • Empty positions will be marked with "."
#
# In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given, you will be receiving
#   coordinates for each of the players. They will be taking turns and stepping on different positions on the board
#   until one of them find the Exit or falls into a Trap.
#
# Here are the rules:
# • If a player hits the letter "E", he escapes the maze and wins the game.
#   - Print "{player} found the Exit and wins the game!" and end the program.
# • If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
#   - Print "{player} is out of the game! The winner is {winner}." and end the program.
# • If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
#   - Print "{player} hits a wall and needs to rest."
# • If a player steps on an empty position ".", nothing happens.
# • Both players can step in the same position at the same time.
#
# Input:
# • On the first line, you will receive "Tom" and "Jerry" separated by ", ". The first player starts first.
# • On the following 6 lines, you will receive the maze board (elements will be separated by a space)
# • On the following lines, you will be receiving coordinates in the format: "({row}, {column})"
#
# Output:
# • You should print the output as described above.
# • The input coordinates will always be valid.
#
#
#
# Tests
#
# Input:
# Tom, Jerry
# . . T . . .
# . . . . . .
# . . W . . .
# . . W . . E
# . . . . . .
# . T . W . .
# (3, 2)
# (1, 3)
# (5, 1)
# (5, 1)
#
# Expected output:
# Tom hits a wall and needs to rest.
# Jerry is out of the game! The winner is Tom.
#
#
#
# Input:
# Jerry, Tom
# . T . . . W
# . . . . T .
# . W . . . T
# . T . E . .
# . . . . . T
# . . T . . .
# (1, 1)
# (3, 0)
# (3, 3)
#
# Expected output:
# Jerry found the Exit and wins the game!
#
#
#
# Input:
# Jerry, Tom
# . . . W . .
# . . T T . .
# . . . . . .
# . T . W . .
# W . . . E .
# . . . W . .
# (0, 3)
# (3, 3)
# (1, 3)
# (2, 2)
# (3, 5)
# (4, 0)
# (5, 3)
# (3, 1)
# (4, 4)
# (4, 4)
#
# Expected output:
# Jerry hits a wall and needs to rest.
# Tom hits a wall and needs to rest.
# Tom hits a wall and needs to rest.
# Jerry hits a wall and needs to rest.
# Tom found the Exit and wins the game!
