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


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
