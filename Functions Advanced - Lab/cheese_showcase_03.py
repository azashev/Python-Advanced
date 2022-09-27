def sorting_cheeses(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for name, quantity in kwargs:
        result.append(name)
        quantities = sorted(quantity, reverse=True)
        result += quantities
    return '\n'.join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
