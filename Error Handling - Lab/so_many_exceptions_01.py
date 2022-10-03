# You are provided with the following code:

# numbers_list = input().split(", ")
# result = 0
#
# for i in range(numbers_list):
#     number = numbers_list[i + 1]
#     if number < 5:
#         result *= number
#     elif number > 5 and number > 10:
#         result /= number
#
# print(result)


# This code raises many exceptions. Fix it, so it works correctly.



numbers_list = [int(x) for x in input().split(", ")]
result = 1

for number in numbers_list:
    if number <= 5:
        result *= number
    elif number < 11:
        result /= number

print(result)



# Examples:
#
# Input                                               Output
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11             0.003968253968253968
# 1, 4, 5                                               20
# 4, 5, 6, 1, 3                                         10
# 2, 5, 10	                                            1
