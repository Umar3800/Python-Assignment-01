#   26.	Write a program to calculate the total salary given basic, HRA (10%), and DA (5%).

salary = int(input("Enter basic salary :"))

HRA = salary * 10 /100
DA = salary * 5 / 100

total_salary = HRA+DA+salary

print("HRA (10%) :",HRA)
print("DA (5%) :",DA)
print(" Total salary :",total_salary)