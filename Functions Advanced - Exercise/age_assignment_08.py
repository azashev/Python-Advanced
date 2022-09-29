def age_assignment(*args, **kwargs):
    names = args
    res = {}
    result = ''

    for name in names:
        first_letter = name[0]
        res[name] = kwargs[first_letter]

    sorted_result = sorted(res.items())

    for name, age in sorted_result:
        result += f"{name} is {age} years old." + '\n'

    return result

print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
