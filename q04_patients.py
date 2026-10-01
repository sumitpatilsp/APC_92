import pandas as pd

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Ramesh", "Sunita", "Alok", "Meena", "Suresh"],
    "Age": [65, 45, 72, 58, 61],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Arthritis"],
    "Medical_Charges": [30000, 5000, 120000, 15000, 55000],
}
df = pd.DataFrame(data)

print("1. Patients above 60 years:\n", df[df["Age"] > 60])
print("\n2. Average medical charge:", df["Medical_Charges"].mean())
print("\n3. Maximum medical charge:", df["Medical_Charges"].max())
print("\n4. Charges > Rs.50,000:\n", df[df["Medical_Charges"] > 50000])
