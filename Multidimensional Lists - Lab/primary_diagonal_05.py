n = int(input())

result = 0

matrix = [[int(x) for x in input().split()] for x in range(n)]

for row in range(n):
    result += matrix[row][row]

print(result)
