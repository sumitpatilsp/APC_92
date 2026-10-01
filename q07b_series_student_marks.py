import pandas as pd

marks = pd.Series({"Aarav": 85, "Diya": 72, "Rohan": 90, "Sneha": 60, "Kabir": 78})

print("Series:\n", marks)
print("\nMarks of Rohan:", marks["Rohan"])
print("\nMaximum:", marks.max(), "->", marks.idxmax())
print("Minimum:", marks.min(), "->", marks.idxmin())
print("\nAverage marks:", marks.mean())
print("\nStudents with marks > 75:\n", marks[marks > 75])
