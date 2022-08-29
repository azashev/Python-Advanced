n = int(input())

even_nums = set()
odd_nums = set()

for row in range(1, n + 1):
    name = input()
    name_ascii_sum = sum([ord(x) for x in name]) // row
    if name_ascii_sum % 2 == 0:
        even_nums.add(name_ascii_sum)
    else:
        odd_nums.add(name_ascii_sum)

sum_even_nums = sum(even_nums)
sum_odd_nums = sum(odd_nums)

if sum_even_nums == sum_odd_nums:
    union = odd_nums.union(even_nums)
    print(*union, sep=', ')
elif sum_even_nums > sum_odd_nums:
    sym_diff = even_nums.symmetric_difference(odd_nums)
    print(*sym_diff, sep=', ')
else:
    difference = odd_nums.difference(even_nums)
    print(*difference, sep=', ')


# You will receive a number N. On the following N lines, you will be receiving names.
# You should sum the ASCII values of each letter in the name and integer divide it to the number of the current
# row (starting from 1). Save the result to a set of either odd or even numbers, depending on if the resulting number is
# odd or even. After that, sum the values of each set.
#
# • If the sums of the two sets are equal, print the union of the values, separated by ", ".
# • If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
# • If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values,
# separated by ", ".
#
# NOTE: On every operation, the starting set should be the odd set
