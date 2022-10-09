def list_manipulator(nums, *args):
    if args[0] == "add":
        if args[1] == "beginning":
            nums = list(args[2:]) + nums
        elif args[1] == "end":
            nums += list(args[2:])
    elif args[0] == "remove":
        if len(args[2:]) > 0:
            index = args[2]
        else:
            index = 0
        if args[1] == "beginning":
            if index > 0:
                nums = nums[index:]
            else:
                nums = nums[1:]

        elif args[1] == "end":
            if index > 0:
                nums = nums[:-index]
            else:
                nums = nums[:-1]

    return nums


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
