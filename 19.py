#   19.	Write a program to calculate the simple interest using the formula SI = (P * R * T) / 100

P = float(input("Enter principle amount :"))
R = float(input("Enter rate amount :"))
T = float(input("Enter Time (in year) :"))

print(f"Simple Interest =",(P*R*T) / 100)