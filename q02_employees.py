import pandas as pd

data = {
    "Employee_ID": [1, 2, 3, 4, 5],
    "Employee_Name": ["Amit", "Priya", "Rahul", "Neha", "Vikram"],
    "Department": ["CSE", "HR", "IT", "Finance", "CSE"],
    "Salary": [65000, 45000, 52000, 48000, 80000],
    "Experience": [5, 3, 7, 4, 10],
}
df = pd.DataFrame(data)

print("1. Salary > Rs.50,000:\n", df[df["Salary"] > 50000])
print("\n2. Average salary:", df["Salary"].mean())
print("\n3. Highest salary:", df["Salary"].max())
print("\n4. Employee with highest experience:\n", df.loc[df["Experience"].idxmax()])

