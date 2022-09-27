def sorting_cheeses(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for name, quantity in kwargs:
        result.append(name)
        quantities = sorted(quantity, reverse=True)
        result += quantities
    return '\n'.join([str(x) for x in result])


# White a function called sorting_cheeses that receives keywords arguments:
# • The key represents the name of the cheese
# • The value is a list of quantities (integers) of the pieces of the given cheese
#
# The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind in
# descending order.
# If two or more cheeses have the same number of pieces, sort them by their names in ascending order (alphabetically).
# For each kind of cheese, return their pieces quantities in descending order.
#
#
# Input:
print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

#
#
#
# Output:
# Camembert
# 500
# 430
# 105
# 100
# 100
# Parmesan
# 135
# 120
# 102
# Mozzarella
# 125
# 50
