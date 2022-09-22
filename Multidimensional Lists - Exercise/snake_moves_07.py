rows, cols = [int(x) for x in input().split()]

snake = list(input())

matrix = []

i = 0

for row in range(rows):
    word = []
    for col in range(cols):
        word.append(snake[i % len(snake)])
        i += 1
    if row % 2 == 0:
        matrix.append(word)
    else:
        matrix.append(word[::-1])

matrix = [''.join(x) for x in matrix]
print(*matrix, sep='\n')
