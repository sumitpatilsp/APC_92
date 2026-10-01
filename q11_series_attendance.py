import pandas as pd

att = pd.Series({"Aditya": 90, "Bhumi": 70, "Chetan": 74, "Divya": 95, "Eshan": 60})

print("Average attendance:", att.mean())
print("\nAttendance below 75%:\n", att[att < 75])
print("\nAttendance above 90%:\n", att[att > 90])
print("\nHighest attendance:", att.idxmax(), "-", att.max())
