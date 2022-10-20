def pawn_move(row, col, turn):
    if turn == 1:
        if board[row - 1][col - 1] == "b":
            return [row - 1, col - 1], True
        elif board[row - 1][col + 1] == "b":
            return [row - 1, col + 1], True
        else:
            return [row - 1, col], False

    elif turn == 2:
        if board[row + 1][col - 1] == "a":
            return [row + 1, col - 1], True
        elif board[row + 1][col + 1] == "a":
            return [row + 1, col + 1], True
        else:
            return [row + 1, col], False


size = 8

board = []

white_positions = []
black_positions = []
board_rows = {
    0: 8,
    1: 7,
    2: 6,
    3: 5,
    4: 4,
    5: 3,
    6: 2,
    7: 1
}
board_cols = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

counter = 1
winner = ""
winner_position = ""

for row in range(size):
    line = input().split()
    if "w" in line:
        white_positions = [row, line.index("w")]
    if "b" in line:
        black_positions = [row, line.index("b")]
    board.append(line)

for turn in range(1, size * 2 - 2):
    if turn % 2 != 0:
        board[white_positions[0]][white_positions[1]] == "-"
        white_capture = False
        white_positions, white_capture = pawn_move(white_positions[0], white_positions[1], 1)
        if white_capture:
            winner_position = board_cols[white_positions[1]] + str(board_rows[white_positions[0]])
            winner = "White"
            print(f"Game over! {winner} win, capture on {winner_position}.")
            break
        if white_positions[0] == 0:
            winner = "White"
            print(f"Game over! {winner} pawn is promoted to a queen at {board_cols[white_positions[1]] + str(board_rows[white_positions[0]])}.")
            break
        board[white_positions[0]][white_positions[1]] = "a"
    else:
        board[black_positions[0]][black_positions[1]] == "-"
        black_capture = False
        black_positions, black_capture = pawn_move(black_positions[0], black_positions[1], 2)
        if black_capture:
            winner = "Black"
            winner_position = board_cols[black_positions[1]] + str(board_rows[black_positions[0]])
            print(f"Game over! {winner} win, capture on {winner_position}.")
            break
        if black_positions[0] == size - 1:
            winner = "Black"
            print(f"Game over! {winner} pawn is promoted to a queen at {board_cols[black_positions[1]] + str(board_rows[black_positions[0]])}.")
            break
        board[black_positions[0]][black_positions[1]] = "b"
