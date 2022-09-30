from collections import deque

def fill_the_box(height, length, width, *args):
    size_of_the_box = height * length * width

    cubes = deque()

    for x in args:
        if x == "Finish":
            break
        else:
            cubes.append(x)

    while cubes:
        if size_of_the_box - cubes[0] > 0:
            size_of_the_box -= cubes.popleft()
        else:
            cubes[0] -= size_of_the_box
            return f"No more free space! You have {sum(cubes)} more cubes."

    return f"There is free space in the box. You could put {size_of_the_box} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
