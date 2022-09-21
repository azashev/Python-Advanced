rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split()] for x in range(rows)]

for col in range(columns):
    result = 0
    for row in range(rows):
        result += matrix[row][col]
    print(result)
