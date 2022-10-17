from collections import deque

def flights(*args):
    flights_info = {}
    args = deque(args)

    while args:
        if args[0] == "Finish":
            break
        destination = args.popleft()
        if destination not in flights_info:
            flights_info[destination] = 0
        flights_info[destination] += args.popleft()

    return flights_info

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))