import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Aditya", "Bhumi", "Chetan", "Divya", "Eshan"],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT"],
    "Total_Classes": [100, 100, 100, 100, 100],
    "Classes_Attended": [90, 70, 74, 95, 60],
}
df = pd.DataFrame(data)
df["Attendance_Percentage"] = df["Classes_Attended"] / df["Total_Classes"] * 100

print(df)
print("\nStudents with attendance below 75%:\n", df[df["Attendance_Percentage"] < 75])
