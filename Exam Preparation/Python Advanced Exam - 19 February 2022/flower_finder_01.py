from collections import deque

vowels = deque(input().split())
consonants = input().split()

flowers = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
found_word = False
result = ''

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for flower in flowers:
        flowers[flower] = flowers[flower].replace(current_vowel, '')
        flowers[flower] = flowers[flower].replace(current_consonant, '')
        if flowers[flower] == '':
            result = flower
            found_word = True

    if found_word:
        break

if found_word:
    print(f"Word found: {result}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
