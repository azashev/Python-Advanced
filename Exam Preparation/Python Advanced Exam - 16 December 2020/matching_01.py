from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    current_male = males[-1]
    current_female = females[0]

    if current_male <= 0 or current_female <= 0:
        if current_male <= 0:
            males.pop()
        if current_female <= 0:
            females.popleft()
        continue

    if current_male % 25 == 0 or current_female % 25 == 0:
        if current_male % 25 == 0:
            males.pop()
            if males:
                males.pop()
        if current_female % 25 == 0:
            females.popleft()
            if females:
                females.popleft()
        continue

    if current_male == current_female:
        matches += 1
        males.pop()
        females.popleft()
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(x) for x in males[::-1])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")
