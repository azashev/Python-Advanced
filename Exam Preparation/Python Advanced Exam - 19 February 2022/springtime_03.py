def start_spring(**kwargs):
    result = ''
    types = {}

    for item, type in kwargs.items():
        if type not in types:
            types[type] = []
        types[type].append(item)

    sorted_types = sorted(types.items(), key=lambda x: (-len(x[1]), x[0]))

    for objects in sorted_types:
        type = objects[0]
        result += f"{type}:\n"
        sorted_objects = sorted(objects[1])
        for object in sorted_objects:
            result += f"-{object}\n"

    return result


# Write a function called start_spring which will receive a different number of keyword arguments.
# Each keyword holds a key with a name of the spring object (string), and each value holds its type (string).
#
# For example, dahlia="flower", shrikes="bird", dogwood="tree".
#
# The function should sort the given spring objects in collections by their type:
# • The collections sorted by their number of elements in descending order.
#   If two or more collections have the same number of elements in them, return them in ascending order (alphabetically)
#   by the type's name.
# • Each collection's elements should be sorted in ascending order (alphabetically) by the object's name.
#
#
# Input:
# • There will be no input. Just parameters passed to your function.
#
# Output:
# • Return the result, sorted as described above in the format:
#   - "{type_one}:
#   -{spring_object_of_this_type_one}
#   -{spring_object_of_this_type_two}
#   ...
#   -{spring_object_of_this_type_N}
#   {type_two}:
#   ...
#   {type_N}:
#   ...
#   -{last_spring_object_of_typeN}"
#
#
#
# Tests:
#
# Input:

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))

#
# Expected output:
# flower:
# -Dahlia
# -Tulip
# -Water Lilly
# bird:
# -Swallows
# -Swifts
# tree:
# -Callery Pear
#
#
#
# Input:

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

#
# Expected output:
# bird:
# -Shrikes
# -Swallow
# -Swallows
# -Thrushes
# -Warblers
# -Woodpeckers
#
#
#
# Input:

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

#
# Expected output:
# bird:
# -Shrikes
# -Swallow
# -Thrushes
# tree:
# -Cherries
# -Magnolia
# -Pear
# insect:
# -Butterfly
