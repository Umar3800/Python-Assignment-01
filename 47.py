#   47.	Write a program to find the geometric mean and harmonic mean of two numbers.

import math

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

geometric_mean = math.sqrt(a * b)
harmonic_mean = (2 * a * b) / (a + b)

print(f"Geometric Mean = {geometric_mean:.2f}")
print(f"Harmonic Mean = {harmonic_mean:.2f}")
