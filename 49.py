#   49.	Write a program to compute the sum of squares of first N even numbers using arithmetic formula.

N = int(input("Enter N: "))

sum_even_squares = 2 * N * (N + 1) * (2 * N + 1) // 3 

print(f"Sum of squares of first {N} even numbers = {sum_even_squares}")
