n = int(input())

matrix = [[int(x) for x in input().split()] for x in range(n)]

sum_primary_diagonal, sum_secondary_diagonal = 0, 0

for row in range(n):
    sum_primary_diagonal += matrix[row][row]
    sum_secondary_diagonal += matrix[row][n - row - 1]

print(abs(sum_primary_diagonal - sum_secondary_diagonal))
