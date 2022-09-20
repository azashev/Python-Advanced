from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_presents = {}

while materials and magic_levels:
    current_material = materials[-1]
    current_magic = magic_levels[0]
    total_magic_level = current_material * current_magic

    if current_material == 0 or current_magic == 0:
        if current_material == 0:
            materials.pop()
        if current_magic == 0:
            magic_levels.popleft()
        continue

    if total_magic_level < 0:
        materials.append(materials.pop() + magic_levels.popleft())
    else:
        if total_magic_level in presents:
            present = presents[total_magic_level]
            if present not in crafted_presents:
                crafted_presents[present] = 1
            else:
                crafted_presents[present] += 1
            materials.pop()
            magic_levels.popleft()
        else:
            materials[-1] += 15
            magic_levels.popleft()

if 'Doll' in crafted_presents and 'Wooden train' in crafted_presents or \
            'Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for present, quantity in sorted(crafted_presents.items()):
    print(f"{present}: {quantity}")
