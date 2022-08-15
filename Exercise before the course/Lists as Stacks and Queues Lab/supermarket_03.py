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


# Write a program that reads lines of input consisting of a customer's name and adds it to the end of a queue until
# "End" is received.
#
# If, in the meantime, you receive the command "Paid", you should print each customer in the order they are served,
# from the first to the last one) and empty the queue.
#
# When you receive "End", you should print the count of the remaining people in the queue in the format:
# "{count} people remaining.".