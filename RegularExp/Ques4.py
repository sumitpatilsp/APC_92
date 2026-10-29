import re
s = input("Enter a string: ")
result = re.findall(r'[A-Z]', s)
print("Uppercase letters:", result)