import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "patients.csv"))

print("1. Patients above 60:\n", df[df["Age"] > 60])
print("\n2. Average medical expense:", df["Medical_Expense"].mean())
print("\n3. Highest expense patient:\n", df.loc[df["Medical_Expense"].idxmax()])
print("\n4. Patients per disease:\n", df["Disease"].value_counts())
print("\n5. Expense > Rs.50,000:\n", df[df["Medical_Expense"] > 50000])
