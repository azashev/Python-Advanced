from functools import reduce

def operate(operator, *args):
    try:
        return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)
    except ZeroDivisionError:
        return reduce(lambda x, y: eval(f"{x} {operator} {y}"), [el for el in args if el != 0])


# Write a function called operate that receives an operator ("+", "-", "*" or "/") as first argument and multiple
# numbers (integers) as additional arguments (*args).
# The function should return the result of the operator applied to all the numbers.
#
#
#
# Test code:
print(operate("+", 1, 2, 3))
print(operate("-", 10, 4))
print(operate("*", 2, 10))
print(operate("/", 20, 2, 2))
#
#
# Output:
# 6
# 6
# 20
# 5.0
