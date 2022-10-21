def words_sorting(*args):
    result = {}
    total_sum = 0
    final_result = ''

    for item in args:
        ascii_value = 0
        for ch in item:
            ascii_value += ord(ch)
        total_sum += ascii_value

        if item not in result:
            result[item] = ascii_value

    if total_sum % 2 == 0:
        result = sorted(result.items(), key=lambda x: x[0])
    else:
        result = sorted(result.items(), key=lambda x: -x[1])

    for item in result:
        name = item[0]
        final_result += f"{name} - "
        count = item[1]
        final_result += f"{count}\n"
    return final_result


# Write a function words_sorting which receives a different number of words.
# Create a dictionary, which will have as keys the words that the function received.
# For each key, create a value that is the sum of all ASCII values of that key.
#
# Then, sort the dictionary:
# • By values in descending order, if the sum of all values of the dictionary is odd
# • By keys in ascending order, if the sum of all values of the dictionary is even
#
#
# Input:
# • There will be no input, just any number of words passed to your function
#
# Output:
# • The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
#
# Constraints:
# • There will be no case with capital letters.
# • There will be no case with a string consisting of other than letters.
#
#
#
# Tests:
#
# Input:
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

#
# Expected output:
# charm - 523
# escape - 625
# mythology - 1004
#
#
#
# Input:
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

#
# Expected output:
# escape - 625
# charm - 523
# eye - 323
#
#
#
# Input:
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

#
# Expected output:
# accolade - 812
# cacophony - 964
