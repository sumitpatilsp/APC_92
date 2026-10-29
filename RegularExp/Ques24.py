import re
s = input("Enter product code: ")
pattern = r'[A-Z]{3}-\d{4}-[A-Z]{2}'
if re.fullmatch(pattern, s):
    print("Valid product code")
else:
    print("Invalid product code")