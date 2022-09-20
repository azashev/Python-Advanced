from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque([x for x in input().split()])

total_honey_made = 0

while working_bees and nectar:
    current_bee = working_bees[0]
    current_nectar = nectar.pop()

    if current_bee > current_nectar:
        continue

    working_bees.popleft()
    symbol = symbols.popleft()
    if symbol == '+':
        total_honey_made += current_bee + current_nectar
    elif symbol == '-':
        total_honey_made += abs(current_bee - current_nectar)
    elif symbol == '*':
        total_honey_made += abs(current_bee * current_nectar)
    elif symbol == '/' and current_nectar > 0:
        total_honey_made += abs(current_bee / current_nectar)


print(f"Total honey made: {total_honey_made}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")

# Worker-bees collect nectar.
# When a worker-bee has found enough nectar, she returns to the hive to drop off the load and pass the nectar to waiting
# bees so they can really start the honey-making process.
#
# You will receive 3 sequences:
# • a sequence of integers, representing working bees
# • a sequence of integers, representing nectar
# • a sequence of symbols – "+", "-", "*" or "/", representing the honey-making process.
#
# Your task is to check if the bee has collected enough nectar to return to the hive and keep track of the total honey
# waiting bees made with the collected nectar.
#
#
# Step one: check if a bee has collected enough nectar.
# You should take the first bee and try to match it with the last nectar:
# • If the nectar value is more or equal to the value of the bee, it is considered collected, and the bee returns to the
# hive to drop off the load (step two).
# • If the nectar value is less than the value of the bee, you should remove the nectar and try to match the bee with
# the next nectar's value until the bee collects enough nectar.
#
#
# Step two: When a bee successfully collects nectar, she returns to the hive, and you should calculate the honey made.
# Take the first symbol in the sequence of symbols ("+", "-", "*" or "/") and make the corresponding calculation:
# "{matched_bee} {symbol} {matched_nectar}"
#
# The result represents the honey that is made from the passed nectar. The calculation should always return the absolute
# value of the result. After the calculation, remove the bee, the nectar, and the symbol.
#
#
# Stop making honey when you are out of bees or nectar.
#
#
# Input:
# • On the first line, you will be given the values of bees - integers, separated by a single space
# • On the second line, you will be given the nectar's values - integers, separated by a single space
# • On the third line, you will be given symbols - "+", "-", "*" or "/", separated by a single space
#
# Output:
# • On the first line - print the total honey made:
#   - "Total honey made: {total honey}"
# • On the next two lines print the bees or the nectar that are left, if there are any, otherwise skip the line:
#   - "Bees left: {bee1}, {bee2}, … {beeN}"
#   - "Nectar left: {nectar1}, {nectar2}, … {nectarN}"
#
# Constraints:
# • All the bee's values will be integers in the range [0, 150]
# • Nectar's values will be integers in the range [0, 150]
# • There always will be enough symbols in the sequence of symbols
