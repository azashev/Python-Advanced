n = int(input())

cars = set()

for _ in range(n):
    direction, car_number = input().split(", ")

    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        cars.remove(car_number)

if cars:
    print('\n'.join(cars))
else:
    print("Parking Lot is Empty")

# Write a program that:
# • Records a car number for every car that enters the parking lot
# • Removes a car number when the car leaves the parking lot
#
# On the first line, you will receive the number of commands - N.
# On the following N lines, you will receive the direction and car's number in the format:
# {direction}, {car_number}"
#
# The direction could only be "IN" or "OUT". Print the car numbers which are still in the parking lot.
# Keep in mind that all car numbers must be unique.
# If the parking lot is empty, print "Parking Lot is Empty".
# Note: The order in which we print the result does not matter and the input will be valid.
