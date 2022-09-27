from functools import reduce

def operate(operator, *args):
    try:
        return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)
    except ZeroDivisionError:
        return reduce(lambda x, y: eval(f"{x} {operator} {y}"), [el for el in args if el != 0])

print(operate("+", 1, 2, 3))
print(operate("-", 10, 4))
print(operate("*", 2, 10))
print(operate("/", 20, 2, 2))
