def intersection(info):
    info = info.split(',')
    current = set(range(int(info[0]), int(info[1]) + 1))
    return current


n = int(input())

longest_intersection = set()

for _ in range(n):
    line = input().split("-")
    first_set = intersection(line[0])
    second_set = intersection(line[1])

    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")


# Write a program that finds the longest intersection. You will be given a number N.
# On each of the next N lines you will be given two ranges in the format:
# {first_start},{first_end}-{second_start},{second_end}
#
# You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
#
# Finally, you should find the longest intersection of all N intersections, print the numbers that are included and its
# length in the format:
# Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}
#
# Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.
