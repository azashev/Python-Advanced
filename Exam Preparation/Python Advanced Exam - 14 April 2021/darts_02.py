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
