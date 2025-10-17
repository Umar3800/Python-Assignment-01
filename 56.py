#   56.	Write a program to compute the distance covered under uniform acceleration using formula s = ut + 1/2 * a * t**2.

u = float(input("Enter initial velocity (u) in m/s: "))
a = float(input("Enter acceleration (a) in m/s²: "))
t = float(input("Enter time (t) in seconds: "))

s = u * t + 0.5 * a * t**2

print(f"Distance covered = {s:.2f} meters")
