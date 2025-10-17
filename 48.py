#   48.	Write a program to compute the sum of the first N natural numbers using arithmetic operators only (no loops).

N = int(input("Enter N: "))

sum_N = N * (N + 1) // 2 

print(f"Sum of first {N} natural numbers = {sum_N}")
