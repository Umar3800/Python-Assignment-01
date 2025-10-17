# 36. Reverse a three-digit number using arithmetic operators

num = int(input("Enter a three-digit number: "))

hundreds = num // 100        
tens = (num // 10) % 10      
units = num % 10             

reversed_num = units * 100 + tens * 10 + hundreds

print(f"Reversed number: {reversed_num}")
