n = int(input())

elements = set()

for _ in range(n):
    current_elements = input().split()
    elements = elements.union(current_elements)

print('\n'.join(elements))

# Write a program that keeps all the unique chemical elements.
# On the first line, you will be given a number n - the count of input lines that you will receive.
# On the following n lines, you will be receiving chemical compounds separated by a single space.
# Your task is to print all the unique ones on separate lines (the order does not matter)
