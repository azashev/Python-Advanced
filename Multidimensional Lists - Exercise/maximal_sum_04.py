from sys import maxsize

rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for x in range(rows)]

result = []
sum = -maxsize

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] +\
                       matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] +\
                       matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum > sum:
            sum = current_sum
            result = [
                [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
            ]

print(f"Sum = {sum}")
[print(*x) for x in result]
