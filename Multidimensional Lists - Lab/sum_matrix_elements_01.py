rows, cols = [int(x) for x in input().split(', ')]

matrix = []
result = 0

for row in range(rows):
    col = [int(x) for x in input().split(', ')]
    result += sum(col)
    matrix.append(col)

# for row in range(rows):
#     for col in range(cols):
#         result += matrix[row][col]

print(result)
print(matrix)
