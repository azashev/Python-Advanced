
clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

used_racks = 1
clothes_sum = 0
while clothes:
    current_clothing = clothes.pop()
    clothes_sum += current_clothing

    if clothes_sum > rack_capacity:
        clothes.append(current_clothing)
        clothes_sum = 0
        used_racks += 1
    elif clothes_sum == rack_capacity:
        continue

print(used_racks)
