# Solution 1

def calculate(nums):
    positives = 0
    negatives = 0
    stronger_is = ''
    for num in nums:
        if num > 0:
            positives += num
        else:
            negatives += num
    if abs(positives) > abs(negatives):
        stronger_is = 'The positives are stronger than the negatives'
    else:
        stronger_is = 'The negatives are stronger than the positives'

    return negatives, positives, stronger_is

numbers = [int(x) for x in input().split()]
sum_of_negatives, sum_of_positives, output = calculate(numbers)

print(sum_of_negatives, sum_of_positives, output, sep='\n')



# Solution 2
#
# def calculate(command, nums):
#     positives = 0
#     negatives = 0
#     stronger_is = ''
#
#     if command == 'positive':
#         result = [x for x in nums if x > 0]
#     else:
#         result = [x for x in nums if x < 0]
#
#     return result
#
# numbers = [int(x) for x in input().split()]
# sum_of_negatives = calculate("negative", numbers)
# sum_of_positives = calculate("positive", numbers)
#
# print(sum(calculate("negative", numbers)))
# print(sum(calculate("positive", numbers)))
#
# if abs(sum(sum_of_positives)) > abs(sum(sum_of_negatives)):
#     print('The positives are stronger than the negatives')
# else:
#     print('The negatives are stronger than the positives')
