#   16.	Write a program to convert a total number of minutes into hours and minutes using // and %.

total = float(input("Enter yours minutes :"))

hours = total//60
minutes = total%60

print(f"your minutes is : {minutes}, your hours is : {hours}")