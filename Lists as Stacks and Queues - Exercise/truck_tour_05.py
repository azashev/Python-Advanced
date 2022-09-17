from collections import deque

number_of_pumps = int(input())
pumps = deque()

for i in range(number_of_pumps):
    pump_data = [int(x) for x in input().split()]
    pumps.append(pump_data)

for attempt in range(number_of_pumps):
    tank = 0
    for current_pump in pumps:
        petrol_refill = current_pump[0]
        distance_to_next_pump = current_pump[1]
        tank += petrol_refill
        if tank < distance_to_next_pump:
            break
        tank -= distance_to_next_pump
    else:
        print(attempt)
        break
    pumps.rotate(-1)
