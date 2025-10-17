#   40.	Write a program to compute the total fuel cost given distance and mileage.

distance = float(input("Enter total distance (in km): "))
mileage = float(input("Enter mileage of vehicle (km per litre): "))
fuel_price = float(input("Enter price of fuel per litre: "))

fuel_needed = distance / mileage

print(f"Total fuel needed: {fuel_needed} litres",
      f"Total fuel cost: ₹{fuel_needed * fuel_price}",sep='\n')
