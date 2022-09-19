n = int(input())

unique_elements = set()

for _ in range(n):
    elements = set(x for x in input().split())
    unique_elements = unique_elements.union(elements)

print(*unique_elements, sep='\n')
