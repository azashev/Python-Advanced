def multiply(*args):
    result = 1

    for num in args:
        result *= num
    return result


# Write a function called multiply that can receive any quantity of numbers (integers) as different parameters and
# returns the result of the multiplication of all of them.
#
#
# Test code:
print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
#
#
# Output
# 20
# 360
# 0
