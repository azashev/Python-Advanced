rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for x in range(rows)]

while True:
    command = input()
    if command == 'END':
        break

    command = command.split()

    if 'swap' not in command or not len(command[1:]) == 4:
        print("Invalid input!")
        continue

    coords = [int(x) for x in command[1:]]
    if False in [
        0 <= coords[0] < rows,
        0 <= coords[1] < cols,
        0 <= coords[2] < rows,
        0 <= coords[3] < cols,
    ]:
        print("Invalid input!")
        continue

    current_num = matrix[coords[0]][coords[1]]
    matrix[coords[0]][coords[1]] = matrix[coords[2]][coords[3]]
    matrix[coords[2]][coords[3]] = current_num
    [print(*x) for x in matrix]
