#   35.	Write a program to find the number of digits in an integer using arithmetic operators only.

num = int(input("Enter an integer: "))

num = abs(num)

count = 0

while num > 0:
    num = num // 10
    count += 1

if count == 0:
    count = 1

print("Number of digits:", count)
