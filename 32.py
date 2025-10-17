#   32.	Write a program to find the power of a number without using ** (using repeated multiplication).

num = int(input("Enter the number :"))
power = int(input("Enter the power :"))

result = 1

for i in range(power) :
      result = result * num
print(f"{num} raised to the power {power} is : {result}")