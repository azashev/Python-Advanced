from collections import deque

queue = deque()

while True:
    name = input()

    if name == "Paid":
        while queue:
            print(queue.popleft())
    elif name == "End":
        count = len(queue)
        print(f"{count} people remaining.")
        break
    else:
        queue.append(name)
