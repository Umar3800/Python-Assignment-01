#   15.	Write a program that takes two numbers and displays (a + b)**2 and (a - b)**2.

a = float(input("Enter First Number :"))
b = float(input("Enter Second Number :"))

cube = (a+b)**2
cube1 = (a-b)**2

print("Additon + Cube :", cube,"Substraction and Cube :",cube1, sep='\n' )