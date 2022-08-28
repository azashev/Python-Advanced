line = input()

chars_count = {}

for ch in line:
    if ch not in chars_count:
        chars_count[ch] = 0
    chars_count[ch] += 1

for key, value in sorted(chars_count.items()):
    print(f"{key}: {value} time/s")


# Write a program that reads a text from the console and counts the occurrences of each character in it.
# Print the results in alphabetical (lexicographical) order.
