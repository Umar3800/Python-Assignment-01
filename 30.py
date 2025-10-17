#   30.	Write a program to find the total and average of N numbers entered by the user.

n = int(input("How many numbers: "))
sum = 0

for i in range(n):
    a = int(input("Enter number: "))
    sum = sum + a

avg = sum / n
print("Total =", sum)
print("Average =", avg)
