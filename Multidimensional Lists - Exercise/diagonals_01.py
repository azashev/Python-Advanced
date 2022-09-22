n = int(input())

matrix = [[int(x) for x in input().split(', ')] for x in range(n)]

primary_diagonal, secondary_diagonal = [], []
sum_primary_diagonal, sum_secondary_diagonal = 0, 0

for row in range(n):
    sum_primary_diagonal += matrix[row][row]
    primary_diagonal.append(matrix[row][row])
    sum_secondary_diagonal += matrix[row][n - row - 1]
    secondary_diagonal.append(matrix[row][n - row - 1])


print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum_primary_diagonal}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum_secondary_diagonal}")
