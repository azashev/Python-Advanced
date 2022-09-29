def even_odd_filter(**kwargs):
    result = {}

    for key, value in kwargs.items():
        if key == "even":
            result[key] = [x for x in value if x % 2 == 0]
        else:
            result[key] = [x for x in value if x % 2 != 0]

    return dict(sorted(result.items(), key=lambda x: len(x[1])))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
