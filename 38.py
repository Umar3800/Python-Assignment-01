#   38.	Write a program to extract and sum all digits of a 4-digit number.

num = int(input("Enter a 4-digit number: "))

d1 = num % 10
d2 = (num // 10) % 10
d3 = (num // 100) % 10
d4 = (num // 1000) % 10


print("Sum of digits =",d1 + d2 + d3 + d4)
