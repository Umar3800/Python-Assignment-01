#   53.	Write a program to compute the area and perimeter of a square when side length is given.

side = float(input("Enter the side length of the square: "))

area = side * side
perimeter = 4 * side

print(f"Area of the square: {area:.2f}")
print(f"Perimeter of the square: {perimeter:.2f}")
