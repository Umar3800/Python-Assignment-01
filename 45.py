#   45.	Write a program to compute the EMI (Equated Monthly Installment) using the standard formula.

P = float(input("Enter principal amount (P): "))
annual_rate = float(input("Enter annual interest rate (in %): "))
N = int(input("Enter number of months: "))

R = annual_rate / (12 * 100)  

EMI = (P * R * (1 + R)**N) / ((1 + R)**N - 1)

print(f"Your EMI is: {EMI}")
