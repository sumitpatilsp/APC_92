import re
s = input("Enter password: ")
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}'
if re.fullmatch(pattern, s):
    print("Strong password")
else:
    print("Weak password")