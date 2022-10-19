from collections import deque

elves_energy = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

counter = 1
created_toys = 0
total_energy_used = 0

while elves_energy and materials:
    current_elf = elves_energy.popleft()
    current_material = materials[-1]

    if current_elf < 5:
        continue

    needed_energy = current_material
    cookie_reward = 1
    current_toys = 1

    if counter % 3 == 0:
        needed_energy *= 2
        current_toys = 2
    if counter % 5 == 0:
        cookie_reward = 0
        current_toys = 0

    if current_elf >= needed_energy:
        created_toys += current_toys
        total_energy_used += needed_energy
        current_elf -= needed_energy
        elves_energy.append(current_elf + cookie_reward)
        materials.pop()
    else:
        elves_energy.append(current_elf * 2)

    counter += 1

print(f"Toys: {created_toys}")
print(f"Energy: {total_energy_used}")

if elves_energy:
    print(f"Elves left: {', '.join(str(x) for x in elves_energy)}")
if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")


# The Christmas elves have special toy-making skills - еach elf can make a toy from a given number of materials.
# First, you will receive a sequence of integers representing each elf's energy.
# On the following line, you will be given another sequence of integers, each representing a number of materials in a
# box.
#
# Your task is to calculate the total elves' energy used for making toys and the total number of successfully made toys.
#
# Take the first elf takes the last box of materials and tries to create the toy:
# • Usually, the elf needs energy equal to the number of materials. If he has enough energy, he makes the toy.
#   His energy decreases by the used energy, and the toy goes straight to Santa's bag.
#   Then, the elf eats a cookie reward which increases his energy by 1, and goes to the end of the line, preparing for
#   the upcoming boxes.
# • Every third time one of the elves takes a box, he tries his best to be creative, and he will need twice as much
#   energy as usual. If he has enough, he manages to create 2 toys. Then, his energy decreases; he eats a cookie reward
#   and goes to the end of the line, similar to the first bullet.
# • Every fifth time one of the elves takes a box, he is a little clumsy and somehow manages to break the toy when he
#   just made it (if he made it). The toy is thrown away, and the elf doesn't get a cookie reward. However, his energy
#   is already spent, and it needs to be added to the total elves' energy.
#   - If an elf creates 2 toys, but he is clumsy, he breaks them.
# •	If an elf does not have enough energy, he leaves the box of materials to the next elf. Instead of making the
#   toy, the elf drinks a hot chocolate which doubles his energy, and goes to the end of the line, preparing for the
#   upcoming boxes.
#
# Note: North Pole's social policy is very tolerant of the elves. If the current elf's energy is less than 5 units, he
# does NOT TAKE a box, but he takes a day off. Remove the elf from the collection.
#
# Stop crafting toys when you are out of materials or elves.
#
#
# Input:
# • The first line of input will represent each elf's energy - integers, separated by a single space
# • On the second line, you will be given the number of materials in each box - integers, separated by a single space
#
# Output:
# • On the first line, print the number of created toys: "Toys: {total_number_of_toys}"
# • On the second line, print the total used energy: "Energy: {total_used_energy}"
# • On the next two lines print the elves and boxes that are left, if there are any, otherwise skip the line:
#   - "Elves left: {elf1}, {elf2}, … {elfN}"
#   - "Boxes left: {box1}, {box2}, … {boxN}"
#
# Constraints:
# • All the elves' values will be integers in the range [1, 100]
# • All the boxes' values will be integers in the range [1, 100]
#
#
#
# Input:
# 10 16 13 25
# 12 11 8
#
# Expected output:
# Toys: 3
# Energy: 31
# Elves left: 3, 6, 26, 14
#
#
#
# Input:
# 10 14 22 4 5
# 11 16 17 11 1 8
#
# Expected output:
# Toys: 7
# Energy: 75
# Elves left: 10, 14
#
#
#
# Input:
# 5 6 7
# 2 1 5 7 5 3
#
# Expected output:
# Toys: 3
# Energy: 20
# Boxes left: 2, 1
