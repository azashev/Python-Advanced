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


# A chessboard has 8 rows and 8 columns.
# Rows, also called ranks, are marked from number 1 to 8, and columns are marked from A to H.
# We have a total of 64 squares.
# Each square is represented by a combination of letters and a number (a1, b1, c1, etc.).
# In this problem colors of the board will be ignored.
#
# We will play the game with two pawns, white (w) and black (b), where they can:
# • Only move forward in a straight line:
#   - White (w) moves from the 1st rank to the 8th rank direction.
#   - Black (b) moves from 8th rank to the 1st rank direction.
# • Can move only 1 square at a time.
# • Can capture another pawn in from of them only diagonally
#
# When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one - this is the 1st
# rank), can be promoted to a queen.
# Two pawns (w and b) will be placed on two random squares of the bord.
# The first move is always made by the white pawn (w), then black moves (b), then white (w) again, and so on.
#
#
# Some rules apply when moving paws:
# • If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn.
#   When a pawn captures another pawn, the game is over.
# • If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
#
#
# Input:
# • On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
#   - Empty positions are marked with "-".
#   - White pawn is marked with "w"
#   - Black pawn is marked with "b"
#
# Output:
# Print either one of the following:
# • If a pawn captures the other, print:
#   - "Game over! {White/Black} win, capture on {square}."
# • If a pawn reaches the last rank, print:
#   - "Game over! {White/Black} pawn is promoted to a queen at {square}."
#
# Constraints:
# • The input will always be valid.
# • The matrix will always be 8x8.
# • There will be no case where two pawns are placed on the same square.
# • There will be no case where two pawns are placed on the same column.
# • There will be no case where black/white will be placed on the last rank.
#
#
#
# Tests:
#
# Input:
# - - - - - - b -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - w - - - - - -
# - - - - - - - -
# - - - - - - - -
#
# Expected output:
# Game over! White pawn is promoted to a queen at b8.
#
#
#
# Input:
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# b - - - - - - -
# - w - - - - - -
# - - - - - - - -
#
# Expected output:
# Game over! White win, capture on a3.
