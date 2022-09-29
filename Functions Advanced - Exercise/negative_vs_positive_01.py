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
