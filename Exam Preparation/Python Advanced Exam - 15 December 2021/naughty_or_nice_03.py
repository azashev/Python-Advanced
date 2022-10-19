from collections import deque

def naughty_or_nice_list(*args, **kwargs):
    kids_lists = {"Nice": [], "Naughty": [], "Not found": []}
    kids = deque(args[0])
    commands = args[1:]
    result = ''

    for x in commands:
        command = x.split('-')
        num = int(command[0])
        current_type = command[1]
        count = 0
        current_kid = ()

        for i in range(len(kids)):
            if num == kids[i][0]:
                count += 1
                current_kid = kids[i]
            if count == 2:
                break
        if count == 1:
            if current_type == 'Naughty':
                kids_lists['Naughty'].append(current_kid[1])
            elif current_type == 'Nice':
                kids_lists['Nice'].append(current_kid[1])
            kids.remove(current_kid)


    for name, current_type in kwargs.items():
        count = 0
        current_kid = ()
        for x in range(len(kids)):
            if kids[x][1] == name:
                count += 1
                current_kid = kids[x]
            if count == 2:
                break
        if count == 1:
            if current_type == 'Naughty':
                kids_lists['Naughty'].append(current_kid[1])
            elif current_type == 'Nice':
                kids_lists['Nice'].append(current_kid[1])
            kids.remove(current_kid)

    while kids:
        kids_lists['Not found'].append(kids.popleft()[1])

    for type, kids in kids_lists.items():
        if kids:
            result += f"{type}: {', '.join(kids)}\n"

    return result


print(naughty_or_nice_list([(3, "Amy"),(1, "Tom"),(7, "George"),(3, "Katy"),],"3-Nice","1-Naughty",Amy="Nice",Katy="Naughty",))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
