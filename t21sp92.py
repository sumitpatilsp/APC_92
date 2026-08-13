roll_no = int(input("Enter roll number: "))
name = input("Enter name: ")
department = input("Enter department: ")
marks = float(input("Enter marks: "))

student = (roll_no, name, department, marks)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])