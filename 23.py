#   23.	Write a program to swap two numbers without using a third variable (using + and -).

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

print("Before swaping a =", a ,"b =",b)

a = a+b
b = a-b
a = a-b

print("After swaping a=",a,"b=",b)
