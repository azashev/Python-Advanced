def func_executor(*args):
    result = ''
    for func in args:
        result += f"{func[0].__name__} - {str(func[0](*func[1]))}" + '\n'
    return result

def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

