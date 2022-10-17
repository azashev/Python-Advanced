size = 7
player_one, player_two = input().split(", ")
matrix = [[x for x in input().split()] for line in range(size)]
matrix = [[int(x) if x.isdigit() else x for x in y ] for y in matrix]


players = {player_one: [501, 0], player_two: [501, 0]}
counter = 1
winner = None
winner_bullseye = None

while True:
    r, c = eval(input())
    if counter % 2 != 0:
        current_player = player_one
    else:
        current_player = player_two
    players[current_player][1] += 1
    counter += 1
    if not 0 <= r < size or not 0 <= c < size:
        continue

    if str(matrix[r][c]).isdigit():
        players[current_player][0] -= int(matrix[r][c])
    elif matrix[r][c] == "D":
        players[current_player][0] -= (matrix[r][0] + matrix[r][-1] + matrix[0][c] + matrix[-1][c]) * 2
    elif matrix[r][c] == "T":
        players[current_player][0] -= (matrix[r][0] + matrix[r][-1] + matrix[0][c] + matrix[-1][c]) * 3
    elif matrix[r][c] == "B":
        winner_bullseye = current_player
        break

    if players[current_player][0] <= 0:
        winner = current_player
        break

if winner_bullseye:
    print(f"{winner_bullseye} won the game with {players[winner_bullseye][1]} throws!")
else:
    print(f"{winner} won the game with {players[winner][1]} throws!")



# You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:
#  1    2    3    4    5    6    7
# 24    D    D    D    D    D    8
# 23    D    T    T    T    D    9
# 22    D    T    B    T    D    10
# 21    D    T    T    T    D    11
# 20    D    D    D    D    D    12
# 19   18   17   16   15   14    13
#
# Each of the two players starts with a score of 501 and they take turns to throw a dart - one throw for each player.
# The score for each turn is deducted from the player’s total score.
# The first player who reduces their score to zero or less wins the game.
#
# You are going to receive the information for every throw on a separate line.
# The coordinate information of a hit will be in the format:
#   "({row}, {column})"
#
# • If a player hits outside the dartboard, he does not score any points.
# • If a player hits a number, it is deducted from his total.
# • If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then deducted from
#   his total.
# • If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then deducted from
#   his total.
# • "B" is the bullseye. If a player hits it, he wins the game, and the program ends.
#
# For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are
#   deducted from his total.
#
# Your job is to find who won the game and with how many turns.
#
# Input:
# • The name of the first player and the name of the second player, separated by ", "
# • 7 lines – the dartboard (separated by single space)
# • On the next lines - the coordinates in the format:
#   "({row}, {column})"
#
# Output:
# • You should print only one line containing the winner and his count of throws:
#   "{name} won the game with {count_turns} throws!"
#
# Constrains:
# • There will always be exactly 7 lines
# • There will always be a winner
# • The points will be in range [1, 24]
# • The coordinates will be in range [0, 100]
#
#
#
#
# Input:
# Ivan, Peter
# 12 21 18 4 20 7 11
# 9 D D D D D 10
# 15 D T T T D 3
# 2 D T B T D 19
# 17 D T T T D 6
# 22 D D D D D 14
# 5 8 23 13 16 1 24
# (3, 3)
#
# Expected output:
# Ivan won the game with 1 throws!
#
#
#
# Input:
# George, Hristo
# 17 8 21 6 13 3 24
# 16 D D D D D 14
# 7 D T T T D 15
# 23 D T B T D 2
# 9 D T T T D 22
# 19 D D D D D 10
# 12 18 4 20 5 11 1
# (1, 0)
# (2, 3)
# (0, 0)
# (4, 2)
# (5, 1)
# (3, 1)
# (0, 0)
# (2, 3)
#
# Expected output:
# Hristo won the game with 4 throws!
