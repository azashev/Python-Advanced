rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    line = input()
    if line == "END":
        break

    line = line.split()
    command = line[0]
    r, c = int(line[1]), int(line[2])
    number = int(line[3])

    if not 0 <= r < rows or not 0 <= c < rows:
        print("Invalid coordinates")
    else:
        if command == "Add":
            matrix[r][c] += number
        elif command == "Subtract":
            matrix[r][c] -= number

[print(*sublist) for sublist in matrix]


# Write a program that reads a matrix from the console and changes its values.
# On the first line, you will get the matrix's rows - N.
# You will get elements for each column on the following N lines, separated with a single space.
#
# You will be receiving commands in the following format:
# • "Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
# • "Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
#
# If the coordinate is invalid, you should print "Invalid coordinates".
# A coordinate is valid if both of the given indexes are in range [0; len() – 1].
#
# When you receive "END", you should print the matrix and stop the program.

#
# Input
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END

# Output:
# 6 2 3
# 4 3 6
# 7 8 9



# Input
# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END

# Output
# Invalid coordinates
# Invalid coordinates
# -41 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 101
