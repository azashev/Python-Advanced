from collections import deque

def best_list_pureness(*args):
    numbers = deque(args[0])
    k = args[1]
    best_pureness = -1
    rotation = 0
    rotations_count = 0

    for i in range(k):
        current_pureness = sum(x*y for x, y in enumerate(numbers))
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            rotation = rotations_count
        numbers.rotate()
        rotations_count += 1

    return f"Best pureness {best_pureness} after {rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
