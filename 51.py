#   51.	Write a program to calculate the factorial of a number using only arithmetic operators and loops.

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i 

print(f"Factorial of {num} is {factorial}")
