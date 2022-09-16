from collections import deque

names = deque()

while True:
    command = input()
    if command == 'End':
        print(f"{len(names)} people remaining.")
        break
    elif command == 'Paid':
        while names:
            print(names.popleft())
    else:
        names.append(command)

