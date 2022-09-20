n = int(input())

parking_lot = set()

for _ in range(n):
    direction, car_number = input().split(', ')
    if direction == "IN":
        parking_lot.add(car_number)
    elif direction == "OUT":
        parking_lot.remove(car_number)

if parking_lot:
    print(*parking_lot, sep='\n')
else:
    print("Parking Lot is Empty")
