from collections import deque

dispenser = int(input())

names = deque()

while True:
    name = input()
    if name == "Start":
        break
    else:
        names.append(name)

while True:
    command = input()
    if command == "End":
        break
    else:
        if command.isdigit():
            liters = int(command)

            if dispenser - liters >= 0:
                dispenser -= liters
                print(f"{names.popleft()} got water")
            else:
                print(f"{names.popleft()} must wait")
        else:
            command = command.split()
            dispenser += int(command[1])
print(f"{dispenser} liters left")