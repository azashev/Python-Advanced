rows, cols = [int(x) for x in input().split(',')]

matrix = [[int(x) for x in input().split(',')] for x in range(rows)]

sum = 0

square = []

for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > sum:
            sum = current_sum
            square = []
            first_list = [matrix[row][col], matrix[row][col + 1]]
            second_list = [matrix[row + 1][col], matrix[row + 1][col + 1]]
            square.append(first_list)
            square.append(second_list)

[print(*list) for list in square]
print(sum)
