import pandas as pd

salary = pd.Series({"Amit": 65000, "Priya": 45000, "Rahul": 52000, "Neha": 48000, "Vikram": 80000})

print("Series:\n", salary)
print("\nHighest salary:", salary.max(), "->", salary.idxmax())
print("Lowest salary:", salary.min(), "->", salary.idxmin())
print("Average salary:", salary.mean())
print("\nEmployees earning > Rs.50,000:\n", salary[salary > 50000])
