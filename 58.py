#   58.	Write a program to simulate a shopping cart total with discount and GST calculation.

n = int(input("Enter number of items: "))
subtotal = 0

for i in range(1, n+1):
    price = float(input(f"Enter price of item {i}: "))
    subtotal += price

discount = float(input("Enter discount percentage: "))
gst = float(input("Enter GST percentage: "))

discounted_price = subtotal * (1 - discount/100)
total_price = discounted_price * (1 + gst/100)

print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Price after discount: ₹{discounted_price:.2f}")
print(f"Total price after GST: ₹{total_price:.2f}")
