import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "students.csv"))

print("1. First 5 records:\n", df.head())
print("\n2. Last 5 records:\n", df.tail())

df["Total"] = df[["Python", "DBMS", "Maths"]].sum(axis=1)
df["Average"] = df["Total"] / 3
print("\n3. Total and average marks:\n", df[["Student_ID", "Name", "Total", "Average"]])

print("\n4. Students with average > 75:\n", df[df["Average"] > 75])
print("\n5. Student with highest average:\n", df.loc[df["Average"].idxmax()])
print("\n6. Subject-wise average:\n", df[["Python", "DBMS", "Maths"]].mean())
