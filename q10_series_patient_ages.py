import pandas as pd

ages = pd.Series({"P101": 65, "P102": 45, "P103": 72, "P104": 58, "P105": 61})

print("Ages:\n", ages)
print("\nAverage age:", ages.mean())
print("Oldest patient:", ages.idxmax(), "-", ages.max())
print("Youngest patient:", ages.idxmin(), "-", ages.min())
print("\nPatients above 60 years:\n", ages[ages > 60])
