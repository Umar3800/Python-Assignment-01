#   54.	Write a program to find the simple and compound interest for multiple years and compare them.

P = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate (%): "))
T = int(input("Enter number of years: "))

SI = (P * R * T) / 100

CI = P * (1 + R/100)**T - P

print(f"Simple Interest = {SI:.2f}")
print(f"Compound Interest = {CI:.2f}")

if CI > SI:
    print("Compound Interest is higher than Simple Interest")
elif CI < SI:
    print("Simple Interest is higher than Compound Interest")
else:
    print("Both interests are equal")

