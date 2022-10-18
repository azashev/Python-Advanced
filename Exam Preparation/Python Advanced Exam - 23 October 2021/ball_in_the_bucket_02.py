def is_valid(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True

matrix = []
points = 0
prize = None

for _ in range(6):
    line = [int(x) if x.isdigit() else x for x in input().split()]
    matrix.append(line)

for _ in range(3):
    row, col = [int(x) for x in input().strip("()").split(", ")]

    if is_valid(row, col) and matrix[row][col] == "B":
        matrix[row][col] = 0
        for r in range(len(matrix)):
            points += matrix[r][col]

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    if points <= 199:
        prize = "Football"
    elif points <= 299:
        prize = "Teddy Bear"
    elif points >= 300:
        prize = "Lego Construction Set"
    print(f"Good job! You scored {points} points, and you've won {prize}.")


# You will be given a matrix with 6 rows and 6 columns representing the board. On the board, there will be
# points (integers) and buckets marked with the letter "B".
#
# Rules of the game:
# • You can throw a ball only 3 times.
# • When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
# • You can hit a bucket only once. If you hit the same bucket again, you do not score any points.
# • If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points.
#
# After the board state, you are going to receive the information for every throw on a separate line.
# The coordinates’ information of a hit will be in the format: "({row}, {column})".
# Depending on how many points you have collected, you win one of the following:
# Football - 100 to 199 points
# Teddy Bear - 200 to 299 points
# Lego Construction Set - 300 and more points
#
# Your job is to keep track of the scored points and to check if you won a prize.
# For more clarifications, see the examples below.
#
#
# Input:
# • 6 lines – matrix representing the board (each position separated by a single space)
# • On the next 3 lines - the coordinates of the throw in the format: "({row}, {column})"
#
# Output:
# • On the first line:
#   - If you won a prize, print:
#       "Good job! You scored {points} points, and you've won {prize}."
#   - If you did not win any prize, print the points you need to get at least the first prize:
#       "Sorry! You need {points} points more to win a prize."
#
# Constraints:
# • All of the given points will be integers in the range [1, 30]
# • All the given indexes will be integers in the range [0, 30]
# • There always will be exactly 6 buckets - 1 on each column
#
#
#
# Input:
# 10 30 B 4 20 24
# 7 8 27 23 11 19
# 13 3 14 B 17 В
# 12 5 21 22 9 6
# B 26 1 28 29 2
# 25 B 16 15 B 18
# (1, 1)
# (20, 15)
# (4, 0)
#
# Expected output:
# Sorry! You need 33 points more to win a prize.
#
#
#
# Input:
# B 30 14 23 20 24
# 29 8 27 18 11 19
# 13 3 B B 17 6
# 28 5 21 22 9 B
# 10 B 26 12 B 2
# 25 1 16 15 7 4
# (0, 0)
# (2, 2)
# (2, 3)
#
# Expected output:
# Good job! You scored 299 points, and you've won Teddy Bear.
