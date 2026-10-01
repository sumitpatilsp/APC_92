import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "employees.csv"))

print("1. CSE employees:\n", df[df["Department"] == "CSE"])
print("\n2. Average salary:", df["Salary"].mean())
print("\n3. Highest salary:", df["Salary"].max(), "| Lowest salary:", df["Salary"].min())
print("\n4. Salary > Rs.50,000:\n", df[df["Salary"] > 50000])
print("\n5. Department-wise average salary:\n", df.groupby("Department")["Salary"].mean())
