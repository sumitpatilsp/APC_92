import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics"],
    "Price": [55000, 500, 1200, 9000, 7500],
    "Quantity": [3, 50, 20, 8, 5],
}
df = pd.DataFrame(data)
df["Total_Amount"] = df["Price"] * df["Quantity"]

print(df)
print("\nProduct with highest total sales:\n", df.loc[df["Total_Amount"].idxmax()])
