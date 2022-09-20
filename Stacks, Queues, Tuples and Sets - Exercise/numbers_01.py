first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
n = int(input())

def action(sequence, numbers, command):
    if command == 'Add First':
        return first_sequence.union(numbers)
    elif command == 'Add Second':
        return second_sequence.union(numbers)
    elif command == 'Remove First':
        return first_sequence.difference(set(numbers))
    elif command == 'Remove Second':
        return second_sequence.difference(set(numbers))


for _ in range(n):
    command = input()
    if 'Add First' in command:
        numbers = [int(x) for x in command.split()[2:]]
        _command = 'Add First'
        first_sequence = action(first_sequence, numbers, _command)
    elif 'Add Second' in command:
        numbers = [int(x) for x in command.split()[2:]]
        _command = 'Add Second'
        second_sequence = action(second_sequence, numbers, _command)
    elif 'Remove First' in command:
        numbers = [int(x) for x in command.split()[2:]]
        _command = 'Remove First'
        first_sequence = action(first_sequence, numbers, _command)
    elif 'Remove Second' in command:
        numbers = [int(x) for x in command.split()[2:]]
        _command = 'Remove Second'
        second_sequence = action(first_sequence, numbers, _command)
    elif command == 'Check Subset':
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
