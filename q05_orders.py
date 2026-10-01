import pandas as pd

data = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005],
    "Customer": ["Anil", "Bhavna", "Chirag", "Deepa", "Esha"],
    "Product": ["Phone", "Headphones", "Tablet", "Charger", "Smartwatch"],
    "Quantity": [1, 2, 1, 3, 1],
    "Price": [15000, 2000, 20000, 600, 4500],
    "Discount": [1000, 200, 2000, 100, 500],
}
df = pd.DataFrame(data)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All orders:\n", df)
print("\nOrders above Rs.5,000:\n", df[df["Final_Amount"] > 5000])
print("\nHighest-value order:\n", df.loc[df["Final_Amount"].idxmax()])
print("\nAverage order value:", df["Final_Amount"].mean())
