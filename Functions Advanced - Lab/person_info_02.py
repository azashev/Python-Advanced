def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"

person = {
"name": "George",
    "town": "Sofia",
    "age": 20
}


# Write a function called get_info that receives a name, age, and a town and returns a string in the format:
# "This is {name} from {town} and he is {age} years old".
# Use dictionary unpacking when testing the function.
#
#
#
# Test code:
print(get_info(**person))
#
#
# Output:
# This is George from Sofia and he is 20 years old
