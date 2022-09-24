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
