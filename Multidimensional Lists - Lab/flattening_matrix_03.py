rows = int(input())

matrix = []

[matrix.extend(int(x) for x in range(rows) for x in input().split(', '))]

# for row in range(rows):
#     matrix.extend([int(x) for x in input().split(', ')])

print(matrix)
