#   55.	Write a program to calculate the depreciation value of an asset using the straight-line method.

CP = float(input("Enter cost price of the asset: "))
SV = float(input("Enter salvage value of the asset: "))
n = int(input("Enter useful life of the asset (in years): "))

depreciation_per_year = (CP - SV) / n

print(f"Depreciation per year = {depreciation_per_year:.2f}")
