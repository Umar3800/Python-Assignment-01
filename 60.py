#   60.	Write a program that accepts three sides of a triangle and determines if it is equilateral, isosceles, or scalene using arithmetic relations.

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("The triangle is Equilateral")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles")
    else:
        print("The triangle is Scalene")
else:
    print("Not a valid triangle")
