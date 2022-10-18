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
