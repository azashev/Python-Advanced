numbers = open('numbers.txt')

print(sum([int(x) for x in numbers]))
numbers.close()


# You are given a file called numbers.txt with the following content:
#
# 1
# 2
# 3
# 4
# 5
#
# Create a program that reads the numbers from the file. Print on the console the sum of those numbers.
