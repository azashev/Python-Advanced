from collections import deque

chocolate = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolate and cups_of_milk and milkshakes < 5:
    current_chocolate = chocolate[-1]
    current_cup_of_milk = cups_of_milk[0]

    if current_chocolate <= 0 or current_cup_of_milk <= 0:
        if current_chocolate <= 0:
            chocolate.pop()
        if current_cup_of_milk <= 0:
            cups_of_milk.popleft()
        continue

    if current_chocolate == current_cup_of_milk:
        milkshakes += 1
        chocolate.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolate[-1] -= 5

print("Great! You made all the chocolate milkshakes needed!" if milkshakes == 5 else "Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print("Milk: empty")
