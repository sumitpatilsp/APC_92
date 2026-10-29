import re
s = input("Enter vehicle number: ")
pattern = r'[A-Z]{2}\d{2}[A-Z]{1,3}\d{4}'
if re.fullmatch(pattern, s):
    print("Valid format")
else:
    print("Invalid format")