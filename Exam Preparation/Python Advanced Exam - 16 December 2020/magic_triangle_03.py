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



# Create a function called get_magic_triangle which will receive a single parameter (integer n) and it should create a
# magic triangle which follows those rules:
# • We start with this simple triangle [[1], [1, 1]]
# • We generate the next rows until we reach n amount of rows
# • Each number in each row is equal to the sum of the two numbers right above it in the triangle
# • If the current number has no neighbor to the upper left/rigth, we just take the existing neighbor
#
# After you create the magic triangle, return it as a multidimensional list. Here is an example with n = 5
#
# Input:
# • There will be no inputs
# • The function will be tested by passing different values of n
# • You can test your function with the test code below
#
# Constraints:
# • N will be in range [2, 100]
#
#
#
# Test code:
# get_magic_triangle(5)
#
# Expected output:
# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
