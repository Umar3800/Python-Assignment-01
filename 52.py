#   52.	Write a program to compute the volume and surface area of a cylinder.

import math

r = float(input("Enter radius of cylinder: "))
h = float(input("Enter height of cylinder: "))

volume = math.pi * r**2 * h
surface_area = 2 * math.pi * r * (r + h)

print(f"Volume of the cylinder: {volume:.2f}")
print(f"Surface area of the cylinder: {surface_area:.2f}")
