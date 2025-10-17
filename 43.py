#   43.	Write a program to calculate the slope of a line passing through two given points.

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

if x2 != x1:
    slope = (y2 - y1) / (x2 - x1)
    print("Slope of the line =", round(slope, 2))
else:
    print("Slope is undefined (vertical line)")
