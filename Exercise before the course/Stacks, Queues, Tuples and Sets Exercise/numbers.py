first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    command = input().split()
    action = command[0]
    seq = command[1]

    if action == "Add":
        if seq == "First":
            [first_sequence.add(int(x)) for x in command[2:]]
        else:
            [second_sequence.add(int(x)) for x in command[2:]]
    elif action == "Remove":
        if seq == "First":
            first_sequence = first_sequence.difference([int(x) for x in command[2:]])
        else:
            second_sequence = second_sequence.difference([int(x) for x in command[2:]])
    elif action == "Check":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')


# First, you will be given two sequences of integers values on different lines.
# The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
#
# Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
# • "Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
# • "Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
# • "Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
# • "Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
# • "Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise,
# print "False".
#
# In the end, print the final sequences, separated by a comma and a space ", "
# The values in each sequence should be sorted in ascending order.
