from collections import deque

names = deque()

quantity_water = int(input())

while True:
    command = input()
    if command == 'Start':
        break
    else:
        names.append(command)

while True:
    command = input()
    if command == 'End':
        break
    command = command.split()
    if 'refill' in command:
        liters = int(command[1])
        quantity_water += liters
    else:
        liters = int(command[0])
        if liters <= quantity_water:
            print(f"{names.popleft()} got water")
            quantity_water -= liters
        else:
            print(f"{names.popleft()} must wait")

print(f"{quantity_water} liters left")
