#   57.	Write a program to calculate speed given distance and time (from multiple trips).

n = int(input("Enter number of trips: "))

for i in range(1, n+1):
    distance = float(input(f"Enter distance for trip {i} (km): "))
    time = float(input(f"Enter time for trip {i} (hours): "))
    speed = distance / time
    print(f"Speed for trip {i} = {speed:.2f} km/h")
