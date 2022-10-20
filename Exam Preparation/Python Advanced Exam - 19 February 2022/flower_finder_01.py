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


# You will be given two sequences of characters, representing vowels and consonants.
# Your task is to start checking if the following words could be found:
# • "rose"
# • "tulip"
# • "lotus"
# • "daffodil"
#
# Start by taking the first character of the vowels collection and the last character from the consonants collection.
# Then check if these letters are present in one or more of the given words.
# If a letter is present, that part of the word is considered found.
# The word is gradually revealed with each letter found.
# Continue processing the next couple of letters until you find one of the given words above.
#
# A letter (vowels or consonants) could participate in more than one word or more than one time in a word, for example:
# • The letter "o" is present in "rose", "lotus", and "daffodil".
# • The letter "l" is present in "tulip", "lotus", and "daffodil".
# • The letter "f" is present in the word "daffodil" twice.
#
# The consonant and the vowel are always removed from the collection after trying to match them with the letters in the
# given words (whether successful or not).
#
# In the end, the program stops when a word is found, or there are no more vowels or consonants.
# As a result, if you found a word, print it and the remaining letters in each collection in the format described below.
# Otherwise, print "Cannot find any word!" on the first line and the remaining letters in each sequence in the format
# described below.
#
#
# Input:
# • On the first line, you will receive vowels, separated by a single space (" ").
# • On the second line, you will receive consonants, separated by a single space (" ").
#
# Output:
# • On the first line:
#   - If a word is found, print it in the format: "Word found: {word_found}"
#   - Otherwise, print: "Cannot find any word!"
# • On the next lines, print the remaining letters in each collection (if there are any left):
#   - "Vowels left: {vowel_one} {vowel_two} … {vowel_N}"
#   - "Consonants left: {consonants_one} {consonants_two} … {consonants_N}"
#
# Constraints:
# • All letters will be lowercase.
# • The letter 'y' will always be a vowel.
# • The letter 'w' will always be a consonant.
#
#
#
# Tests:
#
# Input:
# o e a o e a i
# p r s x r
#
# Expected output:
# Word found: rose
# Vowels left: o e a i
# Consonants left: p r
#
#
#
# Input:
# a a a
# x r l t p p
#
# Expected output:
# Cannot find any word!
# Consonants left: x r l
#
#
#
# Input:
# u a o i u y o e
# p m t l
#
# Expected output:
# Word found: tulip
# Vowels left: u y o e
