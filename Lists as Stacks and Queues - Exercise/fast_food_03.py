from collections import deque

food_quantity = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    if orders[0] <= food_quantity:
        food_quantity -= orders.popleft()
    else:
        break

if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:
    print("Orders complete")
