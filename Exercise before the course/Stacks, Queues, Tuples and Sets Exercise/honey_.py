from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque([x for x in input().split()])

total_honey_made = 0

while working_bees and nectar:
    current_bee = working_bees[0]
    current_nectar = nectar.pop()

    if current_bee > current_nectar:
        continue

    working_bees.popleft()
    symbol = symbols.popleft()
    if symbol == '+':
        total_honey_made += current_bee + current_nectar
    elif symbol == '-':
        total_honey_made += abs(current_bee - current_nectar)
    elif symbol == '*':
        total_honey_made += abs(current_bee * current_nectar)
    elif symbol == '/' and current_nectar > 0:
        total_honey_made += abs(current_bee / current_nectar)


print(f"Total honey made: {total_honey_made}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
