#   22.	Write a program to find the area and circumference of a circle.

import math

R = float(input("Enter the radius of the circle : "))

area =math.pi*R*R
circumference = 2 * math.pi*R

print("area of the circle :", area, "circumfuerence of the circle : ",circumference,sep='\n')