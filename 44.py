#   44.	Write a program to find the profit or loss percentage on selling an item.

cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    profit = sp - cp
    print("Profit =", profit)
    print("Profit % =", (profit / cp) * 100)
elif cp > sp:
    loss = cp - sp
    print("Loss =", loss)
    print("Loss % =", (loss / cp) * 100)
else:
    print("No Profit No Loss")
