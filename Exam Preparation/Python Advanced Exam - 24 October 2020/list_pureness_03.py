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



# Write function called best_list_pureness which will receive a list of numbers and a number K.
# You have to rotate the list K times (last becomes first) to find the variation of the list with the best pureness:
# pureness is calculated by summing all the elements in the list multiplied by their indices.
#
# For example, in the list [4, 3, 2, 6] the best pureness is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26.
#
# At the end the function should return a string containing the highest pureness and the amount of rotations that were
# made to find this pureness in the following format:
# "Best pureness {pureness_value} after {count_rotations} rotations".
#
# If there is more than one highest pureness, take the first one.
#
#
# Input:
# • There will be no input, just parameters passed to your function
#
# Output:
# • There is no expected output
# • The function should return a string in the following format:
# "Best pureness {pureness_value} after {count_rotations} rotations"
#
#
#
# Input:
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
#
# Expected output:
# Best pureness 26 after 3 rotations
#
#
#
# Input:
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
#
# Expected output:
# Best pureness 78 after 2 rotations
#
#
#
# Input:
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
#
# Expected output:
# Best pureness 40 after 0 rotations
