sublists = input().split("|")

result = []

for substring in sublists[::-1]:
    result.extend(substring.split())

print(*result)
