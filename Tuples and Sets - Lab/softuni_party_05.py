number_of_guests = int(input())

guests = set()

for _ in range(number_of_guests):
    guests.add(input())

while True:
    guest = input()
    if guest == "END":
        break
    else:
        guests.remove(guest)
print(len(guests))
print(*sorted(guests), sep='\n')
