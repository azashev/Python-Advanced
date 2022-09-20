rows = int(input())

matrix = [[int(x) for x in input().split(', ') if int(x) % 2 == 0] for row in range(rows)]

print(matrix)



# matrix = []
#
# for x in range(rows):
#     row = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
#     matrix.append(row)
#
# print(matrix)
