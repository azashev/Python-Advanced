from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents = {}

while materials and magic_level:
    current_material = materials.pop()
    current_magic_level = magic_level.popleft()
    current_sum = current_material + current_magic_level

    if current_sum < 100:
        if current_sum % 2 == 0:
            current_sum = current_material * 2 + current_magic_level * 3
        elif current_sum % 2 != 0:
            current_sum *= 2
    elif current_sum > 499:
        current_sum /= 2

    if 100 <= current_sum <= 199:
        if "Gemstone" not in presents:
            presents["Gemstone"] = 0
        presents["Gemstone"] += 1
    elif 200 <= current_sum <= 299:
        if "Porcelain Sculpture" not in presents:
            presents["Porcelain Sculpture"] = 0
        presents["Porcelain Sculpture"] += 1
    elif 300 <= current_sum <= 399:
        if "Gold" not in presents:
            presents["Gold"] = 0
        presents["Gold"] += 1
    elif 400 <= current_sum <= 499:
        if "Diamond Jewellery" not in presents:
            presents["Diamond Jewellery"] = 0
        presents["Diamond Jewellery"] += 1

if "Gemstone" in presents and "Porcelain Sculpture" in presents or "Gold" in presents and "Diamond Jewellery" in presents:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for present, amount in sorted(presents.items()):
    print(f"{present}: {amount}")
