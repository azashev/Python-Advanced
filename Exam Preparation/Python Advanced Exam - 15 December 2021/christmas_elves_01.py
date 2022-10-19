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
