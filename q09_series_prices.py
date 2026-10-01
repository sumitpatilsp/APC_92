import pandas as pd

prices = pd.Series({"Laptop": 55000, "Mouse": 500, "Keyboard": 1200, "Monitor": 9000, "Pen": 20})

print("Products and prices:\n", prices)

prices_increased = prices * 1.10
print("\nPrices after 10% increase:\n", prices_increased)

print("\nMost expensive product:", prices.idxmax(), "-", prices.max())
print("\nProducts costing more than Rs.1,000:\n", prices[prices > 1000])
