#   20.	Write a program to calculate the compound interest using arithmetic operations.

P = float(input("Enter principle amount : "))
R = float(input("Enter rate of amount : "))
T = float(input("Enter time (in year) : "))

A = P* (1+ R / 100) ** T

CI = A - P

print("Compound Interset =",CI )
print("Total Amount =",A)