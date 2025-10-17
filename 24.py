#   24.	Write a program to calculate the BMI (Body Mass Index) of a person using formula BMI = weight / (height ** 2).

weight = float(input("Enter your weight :"))
height = float(input("Enter your height :"))

BMI = weight/(height**2)

print("Body Mass Index :", BMI)
