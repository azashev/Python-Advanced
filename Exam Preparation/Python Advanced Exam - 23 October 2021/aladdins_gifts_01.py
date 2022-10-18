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


# First, you will receive a sequence of integers representing the materials for every wedding present.
# After that, you will be given another sequence of integers – Genie magic level for every aim to make a gift.
#
# Your task is to mix materials with magic levels so you can make presents, listed in the table below.
# Gemstone - 100 to 199
# Porcelain Sculpture - 200 to 299
# Gold - 300 to 399
# Diamond Jewellery - 400 to 499
#
#
# To make a present, you should take the last integer of materials and sum it with the first magic level value.
# If the result is between or equal to the numbers described in the table above, you make the corresponding gift and
# remove both materials and magic value. Otherwise:
# • If the product of the operation is under 100:
#   - And if it is an even number, double the materials, and triple the magic, then sum it again.
#   - And if it is an odd number, double the sum of the materials and the magic level.
#     Then, check again if it is between or equal to any of the numbers in the table above.
# • If the product of the operation is more than 499, divide the sum of the material and the magic level by 2.
#   Then, check again if it is between or equal to any of the numbers in the table above.
# • If, however, the result is not between or equal to any of the numbers in the table above after performing the
#   calculation, remove both the materials and the magic level.
#
# Stop crafting gifts when you are out of materials or magic level.
# You have succeeded in crafting the presents when you've crafted either one of the pairs:
# a gemstone and a sculpture or gold and jewellery.
#
#
# Input:
# • The first line of input will represent the values of materials - integers, separated by a single space
# • On the second line, you will be given the magic levels - integers, separated by a single space
#
# Output:
# • On the first line - print whether you have succeeded in crafting the presents:
#   - "The wedding presents are made!"
#   - "Aladdin does not have enough wedding presents."
# • On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
#   - "Materials left: {material1}, {material2}, …"
#   - "Magic left: {magicValue1}, {magicValue2}, …
# • On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
#   "{present1}: {amount}
#   {present2}: {amount}
#   ...
#   {presentN}: {amount}"
#
# Constraints:
# • All the materials values will be integers in the range [1, 1000]
# • Magic level values will be integers in the range [1, 1000]
#
#
#
# Input:
# 105 20 30 25
# 120 60 11 400 10 1
#
# Expected output:
# The wedding presents are made!
# Magic left: 10, 1
# Gemstone: 1
# Porcelain Sculpture: 2
#
#
#
# Input:
# 30 5 21 6 0 91
# 15 9 5 15 8
#
# Expected output:
# Aladdin does not have enough wedding presents.
# Materials left: 30
# Gemstone: 1
#
#
#
# Input:
# 200
# 5 15 32 20 10 5
#
# Expected output:
# Aladdin does not have enough wedding presents.
# Magic left: 15, 32, 20, 10, 5
# Porcelain Sculpture: 1
