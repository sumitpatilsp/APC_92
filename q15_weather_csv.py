import os
import pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE, "weather.csv"))

print("1. Maximum temperature:", df["Temperature"].max())
print("2. Minimum temperature:", df["Temperature"].min())
print("3. Average temperature:", round(df["Temperature"].mean(), 2))
print("\n4. Records with temperature > 35 C:\n", df[df["Temperature"] > 35])
print("\n5. City-wise average temperature:\n", df.groupby("City")["Temperature"].mean())
