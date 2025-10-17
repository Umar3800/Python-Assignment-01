#   37.	Write a program to check if a number is an Armstrong number (use arithmetic operators only).

num = int(input("Enter a number: "))
temp = num
sum_of_powers = 0
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** digits
    temp //= 10

print(f"{num} is an Armstrong number" if sum_of_powers == num else f"{num} is not an Armstrong number")

