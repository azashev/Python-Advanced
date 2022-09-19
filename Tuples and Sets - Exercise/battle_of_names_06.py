n = int(input())

odd_numbers = set()
even_numbers = set()

for row in range(1, n + 1):
    name = input()
    current_sum = sum([ord(ch) for ch in name]) // row

    if current_sum % 2 == 0:
        even_numbers.add(current_sum)
    else:
        odd_numbers.add(current_sum)

sum_odd = sum(odd_numbers)
sum_even = sum(even_numbers)

if sum_odd == sum_even:
    result = odd_numbers.union(even_numbers)
elif sum_odd > sum_even:
    result = odd_numbers.difference(even_numbers)
else:
    result = odd_numbers.symmetric_difference(even_numbers)

print(*result, sep=', ')
