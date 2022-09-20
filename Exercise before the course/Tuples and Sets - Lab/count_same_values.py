numbers = (float(x) for x in input().split())

nums = {}

for num in numbers:
    if num not in nums:
        nums[num] = 0
    nums[num] += 1

for data in nums.items():
    print(f"{data[0]} - {data[1]} times")


# You will be given numbers separated by a space.
# Write a program that prints the number of occurrences of each number in the format "{number} - {count} times".
# The number must be formatted to the first decimal point.
