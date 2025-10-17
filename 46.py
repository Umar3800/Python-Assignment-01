#   46.	Write a program to compute the perimeter and area of a rectangle using only arithmetic operators and formatted output.

length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))

perimeter = 2 * (length + breadth)
area = length * breadth

print(f"Perimeter of the rectangle: {perimeter}")
print(f"Area of the rectangle: {area}")
