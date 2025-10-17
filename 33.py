#   33.	Write a program to calculate the time taken to cover a distance given speed and distance.

distance = float(input("Enter the distance :"))
speed = float(input("Enter the speed :"))

time = distance/speed

print(f" Your time is : {round(time, 2)}")
