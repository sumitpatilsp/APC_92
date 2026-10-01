import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Aarav", "Diya", "Rohan", "Sneha", "Kabir"],
    "Python": [85, 72, 90, 60, 78],
    "DBMS": [80, 68, 88, 55, 82],
    "Mathematics": [78, 75, 92, 65, 70],
}
df = pd.DataFrame(data)

print("1. DataFrame:\n", df)

df["Total_Marks"] = df[["Python", "DBMS", "Mathematics"]].sum(axis=1)
print("\n2. Total marks:\n", df[["Student_Name", "Total_Marks"]])

df["Average_Marks"] = df["Total_Marks"] / 3
print("\n3. Average marks:\n", df[["Student_Name", "Average_Marks"]])

print("\n4. Students with average > 75%:\n", df[df["Average_Marks"] > 75])
