#   42.	Write a program to compute the distance between two points (x1, y1) and (x2, y2) using the distance formula.

import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance between two points =", round(distance, 2))
