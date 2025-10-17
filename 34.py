#   34.	Write a program to calculate the total cost of items after GST (Goods and Services Tax).

cost = float(input("Enter the cost of the item : "))
gst_percentage = float(input("Enter the GST percentage :"))

gst_amount = (gst_percentage /100) * cost

print(f"Orginal cost : {cost}",
      f"GST {gst_percentage}% : {round(gst_amount, 2)}",
      f"Total cost after GST: {round(cost+gst_amount, 2)}",sep='\n')
