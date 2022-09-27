def recursive_power(num, power):
    result = 1
    if power == 0:
        return result

    result = num * recursive_power(num, power - 1)
    return result


# Create a recursive function called recursive_power() which should receive a number and a power.
# Using recursion, return the result of number ** power.
#
#
# Test code:
print(recursive_power(2, 10))
print(recursive_power(10, 100))
#
#
# Output:
# 1024
# 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
