# Solution 1:

def get_magic_triangle(n):
    matrix = []

    for row in range(1, n + 1):
        line = [1 for x in range(row)]
        matrix.append(line)

    for row in range(2, len(matrix)):
        for col in range(len(matrix[row])):
            if col - 1 > -1:
                if col < len(matrix[row - 1]):
                    matrix[row][col] = matrix[row - 1][col] + matrix[row - 1][col - 1]
                else:
                    matrix[row][col] = matrix[row - 1][col - 1]
            else:
                matrix[row][col] = matrix[row -1][col]

    return matrix

get_magic_triangle(5)


# Solution 2:
#
# def get_magic_triangle(n):
#     matrix = []
#
#     for row in range(n):
#         matrix.append([])
#         matrix[row].append(1)
#
#         for i in range(1, row):
#             matrix[row].append(matrix[row - 1][i] + matrix[row - 1][i - 1])
#         if not row == 0:
#             matrix[row].append(1)
#
#     return print(matrix)
#
# get_magic_triangle(5)
