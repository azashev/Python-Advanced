from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        symbol = symbols.popleft()

        if symbol == '+':
            total_honey += current_bee + current_nectar
        elif symbol == '-':
            total_honey += abs(current_bee - current_nectar)
        elif symbol == '*':
            total_honey += current_bee * current_nectar
        elif symbol == '/' and current_nectar > 0:
            total_honey += abs(current_bee / current_nectar)
    else:
        bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
