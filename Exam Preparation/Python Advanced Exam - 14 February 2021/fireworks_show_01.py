from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

while firework_effects and explosive_power:
    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks[
        "Crossette Fireworks"] >= 3:
        break
    fw_effect = firework_effects.popleft()
    expl_power = explosive_power.pop()
    current_sum = fw_effect + expl_power

    if fw_effect <= 0 or expl_power <= 0:
        if fw_effect <= 0:
            explosive_power.append(expl_power)
        if expl_power <= 0:
            firework_effects.appendleft(fw_effect)
        continue

    if current_sum % 3 == 0 and current_sum % 5 != 0:
        fireworks["Palm Fireworks"] += 1
    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        fireworks["Willow Fireworks"] += 1
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
    else:
        fw_effect -= 1
        firework_effects.append(fw_effect)
        explosive_power.append(expl_power)

if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

for firework, count in fireworks.items():
    print(f"{firework}: {count}")


# First, you will be given a sequence of integers representing firework effects.
# Afterwards you will be given another sequence of integers representing explosive power.
#
# You need to start from the first firework effect and try to mix it with the last explosive power.
# If the sum of their values is:
# • divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
# • divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
# • divisible by both 3 and 5 – create Crossette firework and remove both materials
#
# Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence.
#
# Then, try to mix the same explosive power with the next firework effect.
# If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other.
# When you have successfully prepared enough fireworks for the show or you have no more firework punches or explosive
# power, you need to stop mixing.
#
# To make the perfect firework show, Maria needs 3 of each of the firework types.
#
#
# Input:
# • On the first line, you will receive the integers representing the firework effects, separated by ", ".
# • On the second line, you will receive the integers representing the explosive power, separated by ", ".
#
# Output:
# • On the first line, print:
#   - if Maria successfully prepared the firework show: "Congrats! You made the perfect firework show!"
#   - if Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
# • On the second line, print all firework effects left if there are any:
#   - "Firework Effects left: {effect1}, {effect2}, (…)"
# • On the third line, print all explosive fillings left if there are any:
#   - "Explosive Power left: {filling1}, {filling2}, (…)"
# • Then, you need to print all fireworks and the amount you have of them:
#   - "Palm Fireworks: {count}"
#   - "Willow Fireworks: {count}"
#   - "Crossette Fireworks: {count}"
#
# Constraints:
# • All the given numbers will be integers in the range [-100, 100].
# • There will be no cases with empty sequences.
#
#
#
# Input:
# 5, 6, 4, 16, 11, 5, 30, 2, 3, 27
# 1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
#
# Expected output:
# Congrats! You made the perfect firework show!
# Palm Fireworks: 4
# Willow Fireworks: 3
# Crossette Fireworks: 3
#
#
#
# Input:
# -15, -8, 0, -16, 0, -22
# 10, 5
#
# Expected output:
# Sorry. You can't make the perfect firework show.
# Explosive Power left: 10, 5
# Palm Fireworks: 0
# Willow Fireworks: 0
# Crossette Fireworks: 0
