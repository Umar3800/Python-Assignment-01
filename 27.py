#   27.	Write a program to calculate the final price after a discount percentage is applied.

original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

discount_amount = (discount_percent / 100) * original_price

final_price = original_price - discount_amount

print(f"Discount Amount: ₹{discount_amount:.2f}")
print(f"Final Price after discount: ₹{final_price:.2f}")
