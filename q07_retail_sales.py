import pandas as pd

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Rice Bag", "Soap", "Biscuits", "Cooking Oil", "Sugar"],
    "Category": ["Grocery", "Personal Care", "Snacks", "Grocery", "Grocery"],
    "Price": [1200, 40, 20, 180, 45],
    "Quantity": [15, 100, 200, 60, 120],
}
# 1. Convert to DataFrame
df = pd.DataFrame(data)

# 2 & 3. Add Total_Sales = Price * Quantity
df["Total_Sales"] = df["Price"] * df["Quantity"]
print("DataFrame with Total_Sales:\n", df)

# 4. Sales > Rs.10,000
print("\nProducts with sales > Rs.10,000:\n", df[df["Total_Sales"] > 10000])

# 5. Maximum sales
print("\nProduct with maximum sales:\n", df.loc[df["Total_Sales"].idxmax()])

# 6. Average sales
print("\nAverage sales:", df["Total_Sales"].mean())
