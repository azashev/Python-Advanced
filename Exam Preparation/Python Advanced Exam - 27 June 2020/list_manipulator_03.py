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


# Write a function called list_manipulator which receives a list of numbers as first parameter and different amount of
# other parameters. The second parameter might be "add" or "remove".
#
# The third parameter might be "beginning" or "end". There might or might not be any other parameters (numbers):
# • In case of "add" and "beginning", add the given numbers to the beginning of the given list of numbers and return the new list
# • In case of "add" and "end", add the given numbers to the end of the given list of numbers and return the new list
# • In case of "remove" and "beginning"
#   - If there is another parameter (number), remove that amount of numbers from the beginning of the list of numbers.
#   - If there are no other parameters, remove only the first element of the list.
#   - Finaly, return the new list
#
# •	In case of "remove" and "end"
#   - If there is another parameter (number), remove that amount of numbers from the end of the list of numbers.
#   - Otherwise if there are no other parameters, remove only the last element of the list.
#   - Finaly, return the new list
#
# For more clarifications, see the example test code and output below.
#
#
# Input:
# • There will be no input
# • Parameters will be passed to your function
#
# Output:
# • The function should return the new list of numbers
#
#
#
# Test Code:
# print(list_manipulator([1,2,3], "remove", "end"))
# print(list_manipulator([1,2,3], "remove", "beginning"))
# print(list_manipulator([1,2,3], "add", "beginning", 20))
# print(list_manipulator([1,2,3], "add", "end", 30))
# print(list_manipulator([1,2,3], "remove", "end", 2))
# print(list_manipulator([1,2,3], "remove", "beginning", 2))
# print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
#
#
# Output:
# [1, 2]
# [2, 3]
# [20, 1, 2, 3]
# [1, 2, 3, 30]
# [1]
# [3]
# [20, 30, 40, 1, 2, 3]
# [1, 2, 3, 30, 40, 50]
