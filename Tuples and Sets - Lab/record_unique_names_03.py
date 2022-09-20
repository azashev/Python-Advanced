number_of_names = int(input())

unique_names = set()

for _ in range(number_of_names):
    unique_names.add(input())

print(*unique_names, sep='\n')
