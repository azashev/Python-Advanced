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


# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.
# On the first line, you will receive the starting quantity of water (integer) in a dispenser.
# Then, on the following lines, you will be given the names of some people who want to get water, each on a separate
# line until you receive the command "Start". Add those people in a queue.
#
#
# Finally, you will receive some commands until the command "End":
# 1. "{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in
# the dispenser for that person.
#   - If there is enough water, print "{person_name} got water" and remove him/her from the queue.
#   - Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
#
# 2. "refill {liters}" - add the given litters in the dispenser.
#
# In the end, print how many liters of water have left in the format:
# "{left_liters} liters left".