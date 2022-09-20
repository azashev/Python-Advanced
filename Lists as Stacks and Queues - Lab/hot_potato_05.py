from collections import deque

names = deque([x for x in input().split()])

toss = int(input())

while len(names) > 1:
    names.rotate(-toss)
    print(f"Removed {names.pop()}")

print(f"Last is {''.join(names)}")
